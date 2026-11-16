import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import csv
import os
import random
import hashlib
import time

# Set CustomTkinter appearance
ctk.set_appearance_mode("dark")  # Dark mode for a sleek look
ctk.set_default_color_theme("blue")  # Blue accents for a cool vibe

class WITApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("What Is This? (WIT) Task")
        self.root.geometry("1400x1200")  # Set a larger initial size
        self.root.minsize(600, 400)  # Minimum size for responsiveness

        # Initialize variables for participant and timing
        self.participant_data = {}
        self.stim_start = 0
        self.stim_end = 0

        # Main task variables
        self.drawings = [
            {'drawing_id': 1, 'correct': 'ice cream', 'has_choices': True, 'choices': ['ice cream', 'cloud', 'flower', 'tree', 'hat', 'balloon']},
            {'drawing_id': 2, 'correct': 'lamp', 'has_choices': True, 'choices': ['lamp', 'mushroom', 'umbrella', 'bell', 'guitar', 'tent']},
            {'drawing_id': 3, 'correct': 'train', 'has_choices': True, 'choices': ['train', 'snake', 'ladder', 'car', 'bus', 'submarine']},
            {'drawing_id': 4, 'correct': 'spoon', 'has_choices': True, 'choices': ['spoon', 'leaf', 'knife', 'fork', 'shovel', 'key']},
            {'drawing_id': 5, 'correct': 'boat', 'has_choices': True, 'choices': ['boat', 'shoe', 'fish', 'cup', 'plate', 'bridge']},
            {'drawing_id': 6, 'correct': 'airplane', 'has_choices': False},
            {'drawing_id': 7, 'correct': 'butterfly', 'has_choices': False},
            {'drawing_id': 8, 'correct': 'flower', 'has_choices': False},
            {'drawing_id': 9, 'correct': 'boots', 'has_choices': False},
            {'drawing_id': 10, 'correct': 'lightbulb', 'has_choices': False},
        ]
        self.current_task = 0
        self.current_step = 0

        # Trial (practice) variables
        self.trials = [
            {'drawing_id': '1', 'correct': 'ball', 'has_choices': True, 'choices': ['ice cream', 'cloud', 'flower', 'tree', 'hat', 'balloon']},
            {'drawing_id': '2', 'correct': 'star', 'has_choices': False}
        ]
        self.current_trial = 0
        self.current_trial_step = 0

        # Start with registration frame
        self.create_registration_frame()

    def create_registration_frame(self):
        """Create a modern registration form."""
        self.registration_frame = ctk.CTkFrame(self.root, fg_color="#121212")
        self.registration_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)

        # Title
        ctk.CTkLabel(
            self.registration_frame,
            text="Participant Registration",
            font=("Arial", 20, "bold"),
            text_color="#e0e0e0"
        ).pack(pady=(20, 30))

        # Form fields
        form_frame = ctk.CTkFrame(self.registration_frame, fg_color="#121212")
        form_frame.pack()

        # Name
        ctk.CTkLabel(form_frame, text="Name:", font=("Arial", 14), text_color="#e0e0e0").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.name_entry = ctk.CTkEntry(form_frame, width=300, font=("Arial", 14), corner_radius=10)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Age
        ctk.CTkLabel(form_frame, text="Age:", font=("Arial", 14), text_color="#e0e0e0").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.age_entry = ctk.CTkEntry(form_frame, width=300, font=("Arial", 14), corner_radius=10)
        self.age_entry.grid(row=1, column=1, padx=10, pady=10)

        # Gender
        ctk.CTkLabel(form_frame, text="Gender:", font=("Arial", 14), text_color="#e0e0e0").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.gender_entry = ctk.CTkEntry(form_frame, width=300, font=("Arial", 14), corner_radius=10)
        self.gender_entry.grid(row=2, column=1, padx=10, pady=10)

        # Start button
        ctk.CTkButton(
            self.registration_frame,
            text="Start Task",
            font=("Arial", 14, "bold"),
            fg_color="#00aaff",
            hover_color="#0088cc",
            corner_radius=15,
            command=self.register_participant
        ).pack(pady=30)

    def generate_participant_id(self):
        """Generate a unique participant ID."""
        base_str = f"{self.name_entry.get()}{self.age_entry.get()}{self.gender_entry.get()}{random.getrandbits(32)}"
        return hashlib.sha256(base_str.encode()).hexdigest()[:8]

    def register_participant(self):
        """Validate and register participant."""
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()
        gender = self.gender_entry.get().strip()

        if not all([name, age, gender]):
            messagebox.showerror("Error", "Please fill all fields")
            return

        try:
            int(age)
        except ValueError:
            messagebox.showerror("Error", "Age must be a number")
            return

        self.participant_data = {'id': self.generate_participant_id(), 'name': name, 'age': age, 'gender': gender}
        self.save_participant_data()
        self.registration_frame.destroy()
        # Start with trial phase
        self.create_trial_frame()

    def save_participant_data(self):
        """Save participant data to CSV."""
        file_exists = os.path.exists('wit/participants_wit.csv')
        with open('wit/participants_wit.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(['id', 'name', 'age', 'gender'])
            writer.writerow([self.participant_data['id'], self.participant_data['name'], self.participant_data['age'], self.participant_data['gender']])

    # -------------------- Trial Phase Methods --------------------
    def create_trial_frame(self):
        """Set up the trial interface."""
        self.trial_frame = ctk.CTkFrame(self.root, fg_color="#121212")
        self.trial_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)

        # Top bar with participant ID and progress for trials
        top_bar = ctk.CTkFrame(self.trial_frame, fg_color="#121212")
        top_bar.pack(fill=ctk.X, pady=10)
        ctk.CTkLabel(top_bar, text=f"Participant ID: {self.participant_data['id']}", font=("Arial", 12), text_color="#e0e0e0").pack(side=ctk.LEFT)
        self.trial_progress_label = ctk.CTkLabel(top_bar, text="", font=("Arial", 12), text_color="#e0e0e0")
        self.trial_progress_label.pack(side=ctk.RIGHT)

        # Image frame (fixed size)
        self.trial_image_frame = ctk.CTkFrame(self.trial_frame, width=400, height=400, fg_color="#1e1e1e", corner_radius=10)
        self.trial_image_frame.pack_propagate(False)
        self.trial_image_frame.pack(pady=20)
        self.trial_image_label = ctk.CTkLabel(self.trial_image_frame, text="")
        self.trial_image_label.pack(expand=True)

        # Controls frame for trials
        self.trial_controls_frame = ctk.CTkFrame(self.trial_frame, fg_color="#121212")
        self.trial_controls_frame.pack(fill=ctk.X, pady=10)

        # Initialize trial display
        self.update_trial_display()

    def update_trial_display(self):
        """Update trial display with image and controls."""
        self.stim_start = time.time()
        trial = self.trials[self.current_trial]
        step = self.current_trial_step + 1

        # Load and resize image for trial; images should be placed in images/trial_<drawing_id>/step_<step>.png
        img_path = f"images/trial/trial_{trial['drawing_id']}/step_{step}.png"
        try:
            img = Image.open(img_path)
            ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=(400, 400))
            self.trial_image_label.configure(image=ctk_img)
            # Keep a reference so it's not garbage-collected
            self.trial_image_label.image = ctk_img
        except FileNotFoundError:
            messagebox.showerror("Error", f"Image not found: {img_path}")
            self.next_trial_step()
            return

        # Update progress
        self.trial_progress_label.configure(text=f"Trial {self.current_trial + 1}/{len(self.trials)} | Step {step}/8")

        # Clear previous controls
        for widget in self.trial_controls_frame.winfo_children():
            widget.destroy()

        # Instruction
        ctk.CTkLabel(self.trial_controls_frame, text="Practice: What is this?", font=("Arial", 16, "bold"), text_color="#e0e0e0").pack(pady=10)

        # Response controls
        if trial.get('has_choices', False):
            ctk.CTkLabel(self.trial_controls_frame, text="Select your answer:", font=("Arial", 14), text_color="#e0e0e0").pack(pady=5)
            choices = trial['choices'].copy()
            random.shuffle(choices)
            for choice in choices:
                ctk.CTkButton(
                    self.trial_controls_frame,
                    text=choice,
                    font=("Arial", 14),
                    fg_color="#00aaff",
                    hover_color="#0088cc",
                    corner_radius=15,
                    command=lambda c=choice: self.record_trial_response(c)
                ).pack(pady=5)
        else:
            ctk.CTkLabel(self.trial_controls_frame, text="Enter your answer:", font=("Arial", 14), text_color="#e0e0e0").pack(pady=5)
            self.trial_free_response = ctk.CTkEntry(self.trial_controls_frame, width=300, font=("Arial", 14), corner_radius=10)
            self.trial_free_response.pack(pady=5)
            ctk.CTkButton(
                self.trial_controls_frame,
                text="Submit",
                font=("Arial", 14, "bold"),
                fg_color="#00aaff",
                hover_color="#0088cc",
                corner_radius=15,
                command=self.record_trial_free_response
            ).pack(pady=10)

        # Certainty slider for trial (for example, from 1 to 5)
        ctk.CTkLabel(self.trial_controls_frame, text="Certainty (1-5):", font=("Arial", 14), text_color="#e0e0e0").pack(pady=5)
        self.trial_certainty = ctk.CTkSlider(self.trial_controls_frame, from_=1, to=5, number_of_steps=5, width=300)
        self.trial_certainty.set(3)  # default value
        self.trial_certainty.pack(pady=5)

    def record_trial_response(self, guess):
        """Record multiple-choice response for a trial."""
        self.save_trial_data(guess)
        self.next_trial_step()

    def record_trial_free_response(self):
        """Record free-text response for a trial."""
        guess = self.trial_free_response.get().strip()
        if not guess:
            messagebox.showerror("Error", "Please enter your guess")
            return
        self.save_trial_data(guess)
        self.next_trial_step()

    def save_trial_data(self, guess):
        """Save trial response data to CSV."""
        trial = self.trials[self.current_trial]
        is_correct = (guess.lower() == trial['correct'].lower())
        self.stim_end = time.time()
        exposure_duration = int((self.stim_end - self.stim_start) * 1000)  # in milliseconds
        with open('wit/trial_data_wit.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            # Add a flag (e.g., "trial") to indicate this is a practice trial
            writer.writerow([self.participant_data['id'], trial['drawing_id'], self.current_trial_step + 1, guess, self.trial_certainty.get(), trial.get('has_choices', False), trial['correct'], is_correct, exposure_duration])

    def next_trial_step(self):
        """Advance to next step or trial."""
        self.current_trial_step += 1
        if self.current_trial_step >= 8:
            self.current_trial += 1
            self.current_trial_step = 0
            if self.current_trial >= len(self.trials):
                self.trial_complete()
                return
        self.update_trial_display()

    def trial_complete(self):
        """End trial phase and launch main task."""
        self.trial_frame.destroy()
        self.create_task_frame()

    # -------------------- Main Task Methods --------------------
    def create_task_frame(self):
        """Set up the main task interface."""
        self.task_frame = ctk.CTkFrame(self.root, fg_color="#121212")
        self.task_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)

        # Top bar with participant ID and progress
        top_bar = ctk.CTkFrame(self.task_frame, fg_color="#121212")
        top_bar.pack(fill=ctk.X, pady=10)
        ctk.CTkLabel(top_bar, text=f"Participant ID: {self.participant_data['id']}", font=("Arial", 12), text_color="#e0e0e0").pack(side=ctk.LEFT)
        self.progress_label = ctk.CTkLabel(top_bar, text="", font=("Arial", 12), text_color="#e0e0e0")
        self.progress_label.pack(side=ctk.RIGHT)

        # Image frame (fixed size)
        self.image_frame = ctk.CTkFrame(self.task_frame, width=400, height=400, fg_color="#1e1e1e", corner_radius=10)
        self.image_frame.pack_propagate(False)
        self.image_frame.pack(pady=20)
        self.image_label = ctk.CTkLabel(self.image_frame, text="")
        self.image_label.pack(expand=True)

        # Controls frame
        self.controls_frame = ctk.CTkFrame(self.task_frame, fg_color="#121212")
        self.controls_frame.pack(fill=ctk.X, pady=10)

        # Initialize main task display
        self.update_task_display()

    def update_task_display(self):
        """Update main task display with image and controls."""
        self.stim_start = time.time()
        task = self.drawings[self.current_task]
        step = self.current_step + 1

        # Load and resize image using CTkImage; images should be in images/main/task_<drawing_id>/step_<step>.png
        img_path = f"images/main/task_{task['drawing_id']}/step_{step}.png"
        try:
            img = Image.open(img_path)
            ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=(400, 400))
            self.image_label.configure(image=ctk_img)
            self.image_label.image = ctk_img
        except FileNotFoundError:
            messagebox.showerror("Error", f"Image not found: {img_path}")
            self.next_step()
            return

        # Update progress using self.drawings
        self.progress_label.configure(text=f"Task {self.current_task + 1}/{len(self.drawings)} | Step {step}/8")

        # Clear previous controls
        for widget in self.controls_frame.winfo_children():
            widget.destroy()

        # Instruction
        ctk.CTkLabel(self.controls_frame, text="What is this?", font=("Arial", 16, "bold"), text_color="#e0e0e0").pack(pady=10)

        # Response controls
        if task.get('has_choices', False):
            ctk.CTkLabel(self.controls_frame, text="Select your answer:", font=("Arial", 14), text_color="#e0e0e0").pack(pady=5)
            choices = task['choices'].copy()
            random.shuffle(choices)
            for choice in choices:
                ctk.CTkButton(
                    self.controls_frame,
                    text=choice,
                    font=("Arial", 14),
                    fg_color="#00aaff",
                    hover_color="#0088cc",
                    corner_radius=15,
                    command=lambda c=choice: self.record_response(c)
                ).pack(pady=5)
        else:
            ctk.CTkLabel(self.controls_frame, text="Enter your answer:", font=("Arial", 14), text_color="#e0e0e0").pack(pady=5)
            self.free_response = ctk.CTkEntry(self.controls_frame, width=300, font=("Arial", 14), corner_radius=10)
            self.free_response.pack(pady=5)
            ctk.CTkButton(
                self.controls_frame,
                text="Submit",
                font=("Arial", 14, "bold"),
                fg_color="#00aaff",
                hover_color="#0088cc",
                corner_radius=15,
                command=self.record_free_response
            ).pack(pady=10)

        # Add a certainty slider for main tasks (from 1 to 5)
        ctk.CTkLabel(self.controls_frame, text="Certainty (1-5):", font=("Arial", 14), text_color="#e0e0e0").pack(pady=5)
        self.certainty = ctk.CTkSlider(self.controls_frame, from_=1, to=5, number_of_steps=5, width=300)
        self.certainty.set(3)  # default value
        self.certainty.pack(pady=5)

    def record_response(self, guess):
        """Record multiple-choice response for main tasks."""
        self.save_step_data(guess)
        self.next_step()

    def record_free_response(self):
        """Record free-text response for main tasks."""
        guess = self.free_response.get().strip()
        if not guess:
            messagebox.showerror("Error", "Please enter your guess")
            return
        self.save_step_data(guess)
        self.next_step()

    def save_step_data(self, guess):
        """Save main task response data to CSV."""
        task = self.drawings[self.current_task]
        is_correct = (guess.lower() == task['correct'].lower())
        self.stim_end = time.time()
        exposure_duration = int((self.stim_end - self.stim_start) * 1000)  # in milliseconds
        with open('wit/task_data_wit.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            # Flag as "main" to differentiate from trial responses
            writer.writerow([self.participant_data['id'], task['drawing_id'], self.current_step + 1, guess, self.certainty.get(), task.get('has_choices', False), task['correct'], is_correct, exposure_duration])

    def next_step(self):
        """Advance to next step or main task."""
        self.current_step += 1
        if self.current_step >= 8:
            self.current_task += 1
            self.current_step = 0
            if self.current_task >= len(self.drawings):
                self.task_complete()
                return
        self.update_task_display()

    def task_complete(self):
        """Show completion screen."""
        self.task_frame.destroy()
        completion_frame = ctk.CTkFrame(self.root, fg_color="#121212")
        completion_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)
        ctk.CTkLabel(
            completion_frame,
            text="Task Complete!\nThank you for participating!",
            font=("Arial", 20, "bold"),
            text_color="#e0e0e0"
        ).pack(pady=50)
        ctk.CTkButton(
            completion_frame,
            text="Exit",
            font=("Arial", 14, "bold"),
            fg_color="#00aaff",
            hover_color="#0088cc",
            corner_radius=15,
            command=self.root.destroy
        ).pack(pady=20)

    def run(self):
        self.root.mainloop()

# Initialize CSV files if they don't exist
if not os.path.exists('wit'):
    os.makedirs('wit')

if not os.path.exists('wit/participants_wit.csv'):
    with open('wit/participants_wit.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'name', 'age', 'gender'])

if not os.path.exists('wit/trial_data_wit.csv'):
    with open('wit/trial_data_wit.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['participant_id', 'drawing_id', 'step', 'guess', 'certainty', 'has_choices', 'correct_answer', 'is_correct', 'exposure_duration'])

if not os.path.exists('wit/task_data_wit.csv'):
    with open('wit/task_data_wit.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['participant_id', 'drawing_id', 'step', 'guess', 'certainty', 'has_choices', 'correct_answer', 'is_correct', 'exposure_duration'])

# Run the application
if __name__ == "__main__":
    app = WITApp()
    app.run()
