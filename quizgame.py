import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb

qgame= tk.Tk()
qgame.title("quiz game")
frame = ttk.Frame(qgame, padding="10")
result_label = ttk.Label(frame, text="Generated Password:", font=('Helvetica', 10, 'bold'))
result_label.grid(row=3, column=0, columnspan=2, pady=5)

questions = [
    {"question": "Who is the leader of BTS?", "options": ["A. Kim Seokjin", "B. JK", "C. Jimin","D.Kim Namjoon"], "correct_answer": "D"},
    {"question": "What is the capital of France?", "options": ["A. Berlin", "B. Madrid", "C. Paris","D.Delhi"], "correct_answer": "C"},
    {"question": "What is the largest planet in our solar system?", "options": ["A. Earth", "B. Jupiter", "C. Mars","D. Neptune"], "correct_answer": "B"},
    # Add more questions as needed
]
random.shuffle(questions)
def ask_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    user_answer = input("Your answer (enter the letter corresponding to your choice): ").upper()
    return user_answer == question_data["correct_answer"]
def run_quiz():
    score = 0
    for question in questions:
        if ask_question(question):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['correct_answer']}\n")

    print(f"Quiz complete! Your score is {score}/{len(questions)}.")
run_quiz()


