import pygame
import sys
import random
import time
import csv
from pygame import mixer

# Initialize pygame
pygame.init()
mixer.init()

# Reference screen dimensions
REF_SCREEN_WIDTH = 800
REF_SCREEN_HEIGHT = 600

# Screen setup - make resizable
screen_width, screen_height = REF_SCREEN_WIDTH, REF_SCREEN_HEIGHT
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Probablistic Reward Learnign Task Experiment")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Visual angles calculations
def visual_angle_to_pixels(angle):
    return int(angle * (screen_width / REF_SCREEN_WIDTH * 40))

# Stimuli sizes
fixation_size = visual_angle_to_pixels(0.7)
option_size = visual_angle_to_pixels(2.4)
feedback_font_size = 24

# Positions
center_x, center_y = screen_width // 2, screen_height // 2
option_y = center_y
left_option_x = center_x - int(120 * (screen_width / REF_SCREEN_WIDTH))
right_option_x = center_x + int(120 * (screen_width / REF_SCREEN_WIDTH))

# Fonts
font = pygame.font.SysFont('Arial', 32)
feedback_font = pygame.font.SysFont('Arial', feedback_font_size)
instruction_font = pygame.font.SysFont('Arial', 24)

# Trial parameters
fixation_duration = random.uniform(0.2, 0.3)  # 200-300 ms
options_duration = 0.8  # 800 ms
feedback_duration = 1.0  # 1000 ms

# Experiment parameters
practice_trials = 20  # Now correctly set to 20 trials
trials_per_block = 60
blocks = [
    {"name": "Practice", "probabilities": (0.5, 0.5), "practice": True, "high_shape": "square"},  # Practice first
    {"name": "80/20", "probabilities": (0.8, 0.2), "practice": False, "high_shape": "square"},
    {"name": "50/50", "probabilities": (0.5, 0.5), "practice": False, "high_shape": None}
]

# Points system
POSITIVE_POINTS = 0.50
NEGATIVE_POINTS = -0.25

# Track performance
total_points = 0
current_trial = 0
current_block = 0
in_practice = True

# Data collection
participant_data = []
participant_id = ""
experiment_start_time = 0

# State machine
STATE_ID_INPUT = 0
STATE_INSTRUCTIONS = 1
STATE_FIXATION = 2
STATE_OPTIONS = 3
STATE_QUESTION = 4
STATE_FEEDBACK = 5
STATE_BREAK = 6
STATE_END = 7
current_state = STATE_ID_INPUT
state_start_time = 0

# Trial variables
current_options = []
correct_option = None
feedback = None
response_time = None
selected_option = None
points_earned = 0
id_input = ""

# Instructions (updated to match 20 practice trials)
instructions = [
    "Welcome to the Probablistic Reward Learning Task!",
    "",
    "In this task, you will see two shapes: a circle and a square.",
    "Each shape has a different chance of giving you points.",
    "",
    "Positive outcome: +0.50 points",
    "Negative outcome: -0.25 points",
    "",
    "Your job is to learn which shape gives better rewards over time,",
    "and choose it to maximize your total points.",
    "",
    "Each trial works like this:",
    "1. A fixation cross (+) appears.",
    "2. Two shapes appear briefly — one left, one right.",
    "3. A question mark ('?') means it's time to choose:",
    "   - Press F to choose the LEFT shape.",
    "   - Press J to choose the RIGHT shape.",
    "4. You'll see if you earned or lost points.",
    "",
    "First, you'll complete 20 practice trials (no points).",
    "Then you'll do 2 blocks of 60 trials each.",
    "",
    "Try to earn as many points as you can!",
    "",
    "Press SPACEBAR when you're ready to begin."
]

def draw_fixation():
    pygame.draw.line(screen, RED, (center_x - fixation_size//2, center_y), 
                   (center_x + fixation_size//2, center_y), 3)
    pygame.draw.line(screen, RED, (center_x, center_y - fixation_size//2), 
                   (center_x, center_y + fixation_size//2), 3)

def draw_options():
    for option in current_options:
        if option["shape"] == "circle":
            pygame.draw.circle(screen, WHITE, (option["x"], option["y"]), option_size//2, 3)
        else:
            pygame.draw.rect(screen, WHITE, (option["x"] - option_size//2, option["y"] - option_size//2, 
                                          option_size, option_size), 3)

def draw_question():
    question = font.render("?", True, RED)
    screen.blit(question, (center_x - question.get_width()//2, center_y - question.get_height()//2))

def draw_feedback():
    if feedback is None:
        return
    
    if selected_option is not None:
        option = current_options[selected_option]
        if option["shape"] == "circle":
            pygame.draw.circle(screen, WHITE, (option["x"], option["y"]), option_size//2, 3)
            points_text = f"+{POSITIVE_POINTS:.2f}" if feedback == "positive" else f"{NEGATIVE_POINTS:.2f}"
            points_surface = feedback_font.render(points_text, True, WHITE)
            screen.blit(points_surface, (option["x"] - points_surface.get_width()//2, 
                                       option["y"] - points_surface.get_height()//2))
        else:
            pygame.draw.rect(screen, WHITE, (option["x"] - option_size//2, option["y"] - option_size//2, 
                                          option_size, option_size), 3)
            points_text = f"+{POSITIVE_POINTS:.2f}" if feedback == "positive" else f"{NEGATIVE_POINTS:.2f}"
            points_surface = feedback_font.render(points_text, True, WHITE)
            screen.blit(points_surface, (option["x"] - points_surface.get_width()//2, 
                                       option["y"] - points_surface.get_height()//2))

def draw_too_late():
    message = font.render("Too late!", True, WHITE)
    screen.blit(message, (center_x - message.get_width()//2, center_y - message.get_height()//2))

def draw_break_screen():
    if blocks[current_block]["practice"]:
        message = font.render("Practice complete. Press SPACEBAR to begin the main task.", True, WHITE)
    else:
        message = font.render(f"Block {current_block}/2 complete. Press SPACEBAR to continue.", True, WHITE)
    screen.blit(message, (center_x - message.get_width()//2, center_y - message.get_height()//2))
    points_msg = font.render(f"Current points: {total_points:.2f}", True, WHITE)
    screen.blit(points_msg, (center_x - points_msg.get_width()//2, center_y + 50))

def draw_end_screen():
    screen.fill(BLACK)
    message = font.render("Experiment Complete!", True, WHITE)
    screen.blit(message, (center_x - message.get_width()//2, center_y - 50))
    points_msg = font.render(f"Total Points: {total_points:.2f}", True, WHITE)
    screen.blit(points_msg, (center_x - points_msg.get_width()//2, center_y))
    instruction = font.render("Press ESC to exit", True, WHITE)
    screen.blit(instruction, (center_x - instruction.get_width()//2, center_y + 50))

def draw_id_input():
    screen.fill(BLACK)
    prompt = font.render("Enter Participant ID (PGXX where XX is 11-99):", True, WHITE)
    input_text = font.render(f"PG{id_input}", True, WHITE)
    
    screen.blit(prompt, (center_x - prompt.get_width()//2, center_y - 50))
    screen.blit(input_text, (center_x - input_text.get_width()//2, center_y))
    
    if pygame.time.get_ticks() % 1000 < 500:  # Blinking cursor
        cursor = font.render("_", True, WHITE)
        screen.blit(cursor, (center_x - input_text.get_width()//2 + input_text.get_width(), center_y))

def draw_instructions():
    screen.fill(BLACK)
    for i, line in enumerate(instructions):
        if i < len(instructions) - 1:
            text = instruction_font.render(line, True, WHITE)
            screen.blit(text, (center_x - text.get_width()//2, 50 + i * 30))
        else:
            text = font.render(line, True, WHITE)
            screen.blit(text, (center_x - text.get_width()//2, 50 + i * 30))

def setup_trial():
    global current_options, correct_option, in_practice
    
    block = blocks[current_block]
    probs = block["probabilities"]
    in_practice = block["practice"]
    high_shape = block["high_shape"]
    
    if high_shape == "square":
        shape_probs = {"square": probs[0], "circle": probs[1]}
    elif high_shape == "circle":
        shape_probs = {"circle": probs[0], "square": probs[1]}
    else:
        shape_probs = {"circle": probs[0], "square": probs[1]}
    
    left_shape, right_shape = random.sample(["circle", "square"], 2)
    
    current_options = [
        {"shape": left_shape, "x": left_option_x, "y": option_y, "prob": shape_probs[left_shape]},
        {"shape": right_shape, "x": right_option_x, "y": option_y, "prob": shape_probs[right_shape]}
    ]
    
    correct_option = 0 if current_options[0]["prob"] > current_options[1]["prob"] else 1

def get_feedback(choice):
    if choice < 0 or choice >= len(current_options):
        return None
    prob = current_options[choice]["prob"]
    return "positive" if random.random() < prob else "negative"

def get_relative_time():
    return (time.time() - experiment_start_time) * 1000

def record_trial_data():
    trial_data = {
        "participant_id": participant_id,
        "block": blocks[current_block]["name"],
        "block_number": current_block,
        "trial_number": current_trial + 1,
        "timestamp_ms": int(get_relative_time()),
        "left_option_shape": current_options[0]["shape"],
        "right_option_shape": current_options[1]["shape"],
        "left_option_prob": current_options[0]["prob"],
        "right_option_prob": current_options[1]["prob"],
        "selected_option": selected_option,
        "selected_shape": current_options[selected_option]["shape"] if selected_option is not None else None,
        "response_time_ms": int(response_time) if response_time is not None else None,
        "feedback": feedback,
        "points_earned": points_earned if not in_practice else 0,
        "total_points": total_points if not in_practice else 0,
        "state": current_state,
        "state_duration_ms": int((time.time() - state_start_time) * 1000),
        "is_practice": in_practice
    }
    participant_data.append(trial_data)

def save_data_to_csv():
    filename = f"{participant_id}_PRL.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=participant_data[0].keys())
        writer.writeheader()
        writer.writerows(participant_data)
    print(f"Data saved to {filename}")

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    current_time = time.time()
    state_elapsed = current_time - state_start_time
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.VIDEORESIZE:
            if not event.size[0] == 0 and not event.size[1] == 0:
                screen_width, screen_height = event.size
                screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
                center_x, center_y = screen_width // 2, screen_height // 2
                option_y = center_y
                left_option_x = center_x - int(120 * (screen_width / REF_SCREEN_WIDTH))
                right_option_x = center_x + int(120 * (screen_width / REF_SCREEN_WIDTH))
        
        elif event.type == pygame.KEYDOWN:
            if current_state == STATE_ID_INPUT:
                if event.key == pygame.K_RETURN:
                    if len(id_input) >= 2 and 11 <= int(id_input) <= 99:
                        participant_id = f"PG{id_input}"
                        current_state = STATE_INSTRUCTIONS
                        state_start_time = current_time
                        experiment_start_time = time.time()
                elif event.key == pygame.K_BACKSPACE:
                    id_input = id_input[:-1]
                elif event.unicode.isdigit() and len(id_input) < 2:
                    id_input += event.unicode
            
            elif current_state == STATE_INSTRUCTIONS and event.key == pygame.K_SPACE:
                current_state = STATE_FIXATION
                state_start_time = current_time
                setup_trial()
            
            elif current_state == STATE_QUESTION:
                if event.key == pygame.K_f:
                    selected_option = 0
                    feedback = get_feedback(selected_option)
                    response_time = state_elapsed * 1000
                    if feedback:
                        if not in_practice:
                            points_earned = POSITIVE_POINTS if feedback == "positive" else NEGATIVE_POINTS
                            total_points += points_earned
                        current_state = STATE_FEEDBACK
                        state_start_time = current_time
                elif event.key == pygame.K_j:
                    selected_option = 1
                    feedback = get_feedback(selected_option)
                    response_time = state_elapsed * 1000
                    if feedback:
                        if not in_practice:
                            points_earned = POSITIVE_POINTS if feedback == "positive" else NEGATIVE_POINTS
                            total_points += points_earned
                        current_state = STATE_FEEDBACK
                        state_start_time = current_time
                elif event.key == pygame.K_ESCAPE:
                    running = False
            
            elif current_state == STATE_BREAK and event.key == pygame.K_SPACE:
                current_state = STATE_FIXATION
                state_start_time = current_time
                setup_trial()
                selected_option = None
                feedback = None
                response_time = None
            
            elif current_state == STATE_END and event.key == pygame.K_ESCAPE:
                running = False
    
    # State transitions
    if current_state == STATE_FIXATION and state_elapsed >= fixation_duration:
        current_state = STATE_OPTIONS
        state_start_time = current_time
    
    elif current_state == STATE_OPTIONS and state_elapsed >= options_duration:
        current_state = STATE_QUESTION
        state_start_time = current_time
    
    elif current_state == STATE_QUESTION and state_elapsed >= 1.0:
        current_state = STATE_FEEDBACK
        state_start_time = current_time
        feedback = None
        points_earned = 0
        record_trial_data()
    
    elif current_state == STATE_FEEDBACK and state_elapsed >= feedback_duration:
        record_trial_data()
        current_trial += 1
        
        current_block_trials = practice_trials if in_practice else trials_per_block
        if current_trial >= current_block_trials:
            current_block += 1
            current_trial = 0
            if current_block >= len(blocks):
                current_state = STATE_END
                save_data_to_csv()
            else:
                current_state = STATE_BREAK
                state_start_time = current_time
        else:
            current_state = STATE_FIXATION
            state_start_time = current_time
            setup_trial()
            selected_option = None
            feedback = None
            response_time = None
    
    # Drawing
    screen.fill(BLACK)
    
    if current_state == STATE_ID_INPUT:
        draw_id_input()
    elif current_state == STATE_INSTRUCTIONS:
        draw_instructions()
    elif current_state == STATE_FIXATION:
        draw_fixation()
    elif current_state == STATE_OPTIONS:
        draw_fixation()
        draw_options()
    elif current_state == STATE_QUESTION:
        draw_question()
    elif current_state == STATE_FEEDBACK:
        if feedback is not None:
            draw_feedback()
        else:
            draw_too_late()
    elif current_state == STATE_BREAK:
        draw_break_screen()
    elif current_state == STATE_END:
        draw_end_screen()
    
    if current_state not in [STATE_END, STATE_BREAK, STATE_INSTRUCTIONS, STATE_ID_INPUT] and not in_practice:
        points_text = font.render(f"Points: {total_points:.2f}", True, WHITE)
        screen.blit(points_text, (20, 20))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()