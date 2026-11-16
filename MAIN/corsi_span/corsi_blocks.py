import tkinter as tk
from tkinter import messagebox, ttk
import random
import csv
import time
import os

class CorsiSpanTask:
    def __init__(self, root):
        self.root = root
        self.root.title("Corsi Span Task")
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg="#d3d3d3")
        self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))

        self.sequence_lengths = [2, 3, 4, 5, 6, 7]
        self.max_trials_per_length = 5
        self.length_index = 0
        self.trial_count = 0
        self.correct_count = 0
        self.error_streak = 0
        self.max_correct_span = 0

        self.sequence = []
        self.user_sequence = []
        self.response_phase = False
        self.response_timeout_id = None

        self.practice_phase = True
        # self.practice_sequences = [random.sample(range(16), 2) for _ in range(2)]
        self.practice_sequences = [
            random.sample(range(16), 2),
            random.sample(range(16), 3),
            random.sample(range(16), 3),
            random.sample(range(16), 4),
            random.sample(range(16), 4)
        ]
        self.practice_index = 0

        self.participant_id = ""
        self.result_filename = ""
        self.marker_filename = ""
        self.sequence_start_time = None
        self.response_start_time = None
        self.experiment_start_time = None

        self.canvas = None
        self.rectangles = []
        self.rect_id_to_index = {}

        self.create_positions()
        self.create_welcome_screen()

    def create_positions(self):
        self.positions = []
        grid_size = 4
        block_size = 150
        padding = 15
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        total_width = grid_size * block_size + (grid_size - 1) * padding
        total_height = grid_size * block_size + (grid_size - 1) * padding
        offset_x = (screen_width - total_width) // 2
        offset_y = (screen_height - total_height) // 2
        for i in range(grid_size):
            for j in range(grid_size):
                x = offset_x + j * (block_size + padding)
                y = offset_y + i * (block_size + padding)
                self.positions.append((x, y))

    def create_welcome_screen(self):
        self.clear_screen()
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(expand=True)

        ttk.Label(frame, text="Participant ID:", font=("Arial", 12)).pack(anchor='w')
        self.pid_entry = ttk.Entry(frame, font=("Arial", 12))
        self.pid_entry.pack(fill='x', pady=5)

        ttk.Label(frame, text="Name:", font=("Arial", 12)).pack(anchor='w')
        self.name_entry = ttk.Entry(frame, font=("Arial", 12))
        self.name_entry.pack(fill='x', pady=5)

        ttk.Label(frame, text="Age:", font=("Arial", 12)).pack(anchor='w')
        vcmd = (self.root.register(lambda P: P.isdigit() or P == ""), "%P")
        self.age_entry = ttk.Entry(frame, font=("Arial", 12), validate="key", validatecommand=vcmd)
        self.age_entry.pack(fill='x', pady=5)

        ttk.Label(frame, text="Gender:", font=("Arial", 12)).pack(anchor='w')
        self.gender_var = tk.StringVar()
        self.gender_combo = ttk.Combobox(frame, textvariable=self.gender_var,
                                         values=["Male", "Female", "Other"], font=("Arial", 12), state="readonly")
        self.gender_combo.pack(fill='x', pady=5)

        ttk.Button(frame, text="Start", command=self.save_participant_data).pack(pady=20)

    def save_participant_data(self):
        pid = self.pid_entry.get().strip()
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()
        gender = self.gender_var.get().strip()

        if not pid or not name or not age or not gender:
            messagebox.showerror("Error", "Please fill all fields.")
            return

        self.participant_id = pid
        self.result_filename = f"{pid}_results.csv"
        self.marker_filename = f"{pid}_markers.csv"
        self.experiment_start_time = time.time()

        file_exists = os.path.exists("participants.csv")
        with open("participants.csv", "a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Participant ID", "Name", "Age", "Gender", "Max Span"])
            writer.writerow([pid, name, age, gender, ""])

        with open(self.result_filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([ 
                "Participant ID",
                "Length", "Trial", "Sequence", "User Sequence", "Correct",
                             "Seq Start", "Resp Start", "Resp End"])

        with open(self.marker_filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp (ms)", "Marker"])

        self.show_instructions()
    def show_instructions(self):
        self.clear_screen()
        instruction_text = (
            "You will see a set of blue blocks on the screen.\n\n"
            "Some of these blocks will light up one by one in a specific sequence:\n"
            "- Blocks will turn YELLOW as they flash during the sequence.\n"
            "- The LAST block will turn GREEN to mark the end of the sequence.\n\n"
            "After the flashing ends, your task is to click the same blocks in the same order.\n\n"
            "The sequence length will start from 2 and increase up to 10.\n"
            "To move to the next sequence length, you need to get 3 correct responses for the current length.\n"
            "If you get 3 incorrect responses in a row at the same length, the task will end early.\n\n"
            "Click 'OK' when you're ready to begin practice."
        )
        frame = ttk.Frame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor='center')
        label = ttk.Label(frame, text=instruction_text, justify="center", wraplength=800, font=("Arial", 14))
        label.pack(pady=20)
        ttk.Button(frame, text="OK", command=self.start_practice).pack(pady=10)

    def start_practice(self):
        self.clear_screen()
        self.create_canvas()
        self.header_label = tk.Label(self.root, text="Practice Trial", font=("Arial", 20, "bold"), bg="#d3d3d3")
        self.header_label.place(relx=0.5, y=10, anchor='n')
        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 16), bg="#d3d3d3")
        self.feedback_label.place(relx=0.5, y=50, anchor='n')
        self.sequence = self.practice_sequences[self.practice_index]
        self.user_sequence = []
        self.flash_sequence(0)

    def start_task(self):
        self.practice_phase = False
        self.length_index = 0
        self.trial_count = 0
        self.correct_count = 0
        self.error_streak = 0
        self.clear_screen()
        self.create_canvas()
        self.header_label = tk.Label(self.root, text=f"Participant ID: {self.participant_id}", font=("Arial", 16), bg="#d3d3d3")
        self.header_label.place(relx=0.5, y=10, anchor='n')
        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 16), bg="#d3d3d3")
        self.feedback_label.place(relx=0.5, y=50, anchor='n')
        self.root.after(1000, self.show_sequence)

    def show_sequence(self):
        if self.practice_phase:
            self.sequence = self.practice_sequences[self.practice_index]
        else:
            if self.length_index >= len(self.sequence_lengths):
                return self.end_task()

            

            self.sequence = random.sample(range(16), self.sequence_lengths[self.length_index])

        self.user_sequence = []
        self.sequence_start_time = time.time()
        self.flash_sequence(0)


   
    
    def flash_sequence(self, index):
        if index >= len(self.sequence):
            return

        current = self.sequence[index]
        color = "#00FF00" if index == len(self.sequence) - 1 else "#FFD700"
        self.canvas.itemconfig(self.rectangles[current], fill=color)

        if index == len(self.sequence) - 1:
            # After 500ms, reset green block and then enable response
            self.root.after(500, lambda: (self.reset_block(current, index), self.enable_response()))
        else:
            self.root.after(500, lambda: self.reset_block(current, index))


   

    def reset_block(self, idx, index):
        self.canvas.itemconfig(self.rectangles[idx], fill="#007BFF")
        self.root.after(500, lambda: self.flash_sequence(index + 1))



    def enable_response(self):
        self.response_phase = True
        self.response_start_time = time.time()
        self.log_marker("RESPONSE_START")
        self.canvas.bind("<Button-1>", self.handle_canvas_click)
        self.response_timeout_id = self.root.after(20000, self.evaluate_response_if_incomplete)

    def handle_canvas_click(self, event):
        if not self.response_phase:
            return
        clicked_items = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)
        for item in clicked_items:
            if item in self.rect_id_to_index:
                idx = self.rect_id_to_index[item]
                self.user_sequence.append(idx)
                self.log_marker(f"CLICK_{idx}")
                self.canvas.itemconfig(item, fill="green")
                self.root.after(300, lambda rect=item: self.canvas.itemconfig(rect, fill="#007BFF"))
                break
        if len(self.user_sequence) == len(self.sequence):
            self.canvas.unbind("<Button-1>")
            if self.response_timeout_id:
                self.root.after_cancel(self.response_timeout_id)
            self.evaluate_response()

    def evaluate_response_if_incomplete(self):
        if self.response_phase:
            self.canvas.unbind("<Button-1>")
            self.evaluate_response()

    def evaluate_response(self):
        self.response_phase = False
        correct = self.user_sequence == self.sequence
        self.feedback_label.config(text="Correct" if correct else "Incorrect", fg="green" if correct else "red")
        self.log_marker("RESPONSE_END")
        if not self.practice_phase:
            self.log_result(correct)
        # self.root.after(1000, lambda: self.clear_feedback_and_continue(correct))
        self.root.after(300, lambda: self.root.after(200, lambda: self.clear_feedback_and_continue(correct)))


    

    def clear_feedback_and_continue(self, correct):
        self.feedback_label.config(text="")

        if self.practice_phase:
            self.practice_index += 1
            if self.practice_index >= len(self.practice_sequences):
                return self.show_practice_end_message()
            else:
                self.sequence = self.practice_sequences[self.practice_index]
                self.root.after(1000, self.show_sequence)
        else:
            self.trial_count += 1

            if correct:
                self.correct_count += 1
                self.error_streak = 0
            else:
                self.error_streak += 1

            #  If 3 correct → move to next length
            if self.correct_count >= 3:
                self.max_correct_span = max(self.max_correct_span, self.sequence_lengths[self.length_index])
                self.length_index += 1
                self.trial_count = 0
                self.correct_count = 0
                self.error_streak = 0
                self.root.after(1000, self.show_sequence)
                return

            #  If 2 wrong in a row → end experiment
            if self.error_streak >= 3:
                return self.end_task()

            # Otherwise continue with same length
            self.root.after(1000, self.show_sequence)



    

    def show_practice_end_message(self):
        self.clear_screen()

        label = tk.Label(self.root,
                        text="Practice Completed.\nNow the actual experiment will begin.",
                        font=("Arial", 20),
                        bg="#d3d3d3", justify="center")
        label.place(relx=0.5, rely=0.5, anchor="s")  # Align bottom of label at center

        start_button = tk.Button(self.root,
                                text="Start Experiment",
                                font=("Arial", 14),
                                bg="#007BFF",      # Bootstrap blue
                                fg="white",
                                activebackground="#0056b3",
                                activeforeground="white",
                                relief="flat",
                                command=self.start_task)
        start_button.place(relx=0.5, rely=0.5, anchor="n")  # Align top of button at center



    def log_result(self, correct):
        current_length = self.sequence_lengths[self.length_index]
        seq_start = int((self.sequence_start_time - self.experiment_start_time) * 1000)
        resp_start = int((self.response_start_time - self.experiment_start_time) * 1000)
        resp_end = int((time.time() - self.experiment_start_time) * 1000)
        with open(self.result_filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                self.participant_id,
                current_length, self.trial_count, self.sequence, self.user_sequence,
                "Correct" if correct else "Incorrect", seq_start, resp_start, resp_end
            ])

    def log_marker(self, marker):
        timestamp = int((time.time() - self.experiment_start_time) * 1000)
        with open(self.marker_filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, marker])

    def end_task(self):
        if os.path.exists("participants.csv"):
            with open("participants.csv", "r") as file:
                lines = list(csv.reader(file))
            with open("participants.csv", "w", newline="") as file:
                writer = csv.writer(file)
                for row in lines:
                    if row and row[0] == self.participant_id:
                        row[-1] = str(self.max_correct_span)
                    writer.writerow(row)
        self.clear_screen()
        ttk.Label(self.root, text=f"Task Completed!\nMax Span: {self.max_correct_span}", font=("Arial", 20)).pack(pady=20)
        ttk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=20)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_canvas(self):
        self.canvas = tk.Canvas(self.root, bg="#d3d3d3", highlightthickness=0)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self.rectangles = []
        self.rect_id_to_index = {}
        for idx, (x, y) in enumerate(self.positions):
            rect = self.canvas.create_rectangle(x, y, x + 150, y + 150, fill="#007BFF", outline="black", width=2)
            self.rectangles.append(rect)
            self.rect_id_to_index[rect] = idx

if __name__ == "__main__":
    root = tk.Tk()
    app = CorsiSpanTask(root)
    root.mainloop()
