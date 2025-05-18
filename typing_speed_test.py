import tkinter as tk
import time
import random

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test Game")
        self.root.geometry("700x300")
        self.root.resizable(False, False)

        self.sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "Typing speed tests are a fun way to improve your skills.",
            "Practice makes perfect when it comes to typing fast.",
            "Python programming is both fun and powerful.",
            "Artificial intelligence is transforming the world."
        ]

        self.current_sentence = ""
        self.start_time = 0
        self.end_time = 0

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Typing Speed Test Game", font=("Helvetica", 20))
        self.title_label.pack(pady=10)

        self.sentence_label = tk.Label(self.root, text="", font=("Helvetica", 16), wraplength=650)
        self.sentence_label.pack(pady=10)

        self.entry = tk.Text(self.root, height=3, width=80, font=("Helvetica", 14))
        self.entry.pack(pady=10)
        self.entry.config(state=tk.DISABLED)

        self.start_button = tk.Button(self.root, text="Start Test", command=self.start_test, font=("Helvetica", 14))
        self.start_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

    def start_test(self):
        self.entry.config(state=tk.NORMAL)
        self.entry.delete("1.0", tk.END)
        self.result_label.config(text="")
        self.current_sentence = random.choice(self.sentences)
        self.sentence_label.config(text=self.current_sentence)
        self.start_time = time.time()
        self.start_button.config(state=tk.DISABLED)
        self.entry.focus_set()
        self.entry.bind("<Return>", self.end_test)

    def end_test(self, event):
        self.end_time = time.time()
        typed_text = self.entry.get("1.0", tk.END).strip()
        self.entry.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.entry.unbind("<Return>")

        time_taken = self.end_time - self.start_time
        words = len(self.current_sentence.split())
        wpm = (len(typed_text.split()) / time_taken) * 60
        accuracy = self.calculate_accuracy(self.current_sentence, typed_text)

        result_text = f"Time: {time_taken:.2f} seconds | Speed: {wpm:.2f} WPM | Accuracy: {accuracy:.2f}%"
        self.result_label.config(text=result_text)

    def calculate_accuracy(self, original, typed):
        original_words = original.split()
        typed_words = typed.split()
        correct_words = 0
        for o, t in zip(original_words, typed_words):
            if o == t:
                correct_words += 1
        accuracy = (correct_words / len(original_words)) * 100
        return accuracy

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
