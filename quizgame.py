import random
import tkinter as tk
from tkinter import ttk
qgame = tk.Tk()
qgame.geometry('500x500')
class QuizGame:
    def __init__(self):
        self.questions = [
            {"question": "Who is the leader of BTS?", "options": ["A. KIM SEOKJIN", "B. YOONGI", "C. KIM NAMJOON"], "correct_answer": "C"},
            {"question": "Which year BTS debuted?", "options": ["A. 2004", "B. 2013", "C. 2007"], "correct_answer": "B"},
            {"question": "What is Maknae of BTS?", "options": ["A. v", "B. Jk", "C. Jhope"], "correct_answer": "B"},
            {"question": "Who is the oldest in BTS?", "options": ["A. KIM SEOKJIN", "B. JK", "C. JIMIN"], "correct_answer": "A"},
            {"question": "What is BTS first song?", "options": ["A. DYNAMITE", "B. NO MORE DREAM", "C. 3D"], "correct_answer": "B"},
            {"question": "In which year did BTS release PROOF album?", "options": ["A. 2020", "B. 2021", "C. 2022"], "correct_answer": "C"},
        ]
Frame = tk.Frame(qgame, padx=10, pady=10, bg='blue')
question_Label= tk.Label(Frame, height=5, width=25, bg='black')
option1 = tk.Button(Frame, font=('verdena',20))
option2 = tk.Button(Frame, font=('verdena',20))
option3 = tk.Button(Frame, font=('verdena',20))

Button_next = tk.Button(Frame,text='NEXT', font=('verdana',20))
Frame.pack(fill="both", expand="true")
question_Label.grid(row=1, column=0)

option1.grid(row=1, column=0)
option2.grid(row=2, column=0)
option3.grid(row=3, column=0)
Button_next.grid(row=4, column=0)
    
def display_welcome(self):
    print("Welcome to the Quiz Game!")
    print("You will be asked multiple-choice questions. Choose the correct answer.")

def present_questions(self):
    random.shuffle(self.questions)
    for question_data in self.questions:
        print("\n" + "=" * 40)
        print(question_data['question'])
        print("-" * 40)
        for option in question_data['options']:
            print(option)

            user_answer = input("\nYour answer: ").upper()
            self.evaluate_answer(user_answer, question_data['correct_answer'])

def evaluate_answer(self, user_answer, correct_answer):
    if user_answer == correct_answer:
            print("Correct!")
            self.score += 1
    else:
            print(f"Wrong! The correct answer is {correct_answer}")

def display_final_results(self):
    print("\n" + "=" * 40)
    print(f"Quiz Complete! Your final score is {self.score}/{len(self.questions)}")
    if self.score == len(self.questions):
            print("Congratulations! You got all the questions right.")
    elif self.score >= len(self.questions) / 2:
            print("Good job! You did well.")
    else:
            print("Keep practicing. You can do better!")

def play_again(self):
        play_again = input("Do you want to play again? (yes/no): ").lower()
        return play_again == 'yes'

def run_quiz(self):
    self.score = 0
    self.display_welcome()

    while True:
        self.present_questions()
        self.display_final_results()

        if not self.play_again():
                print("Thanks for playing! Goodbye.")
                break

if __name__ == "__main__":
    quiz_game = QuizGame()
    quiz_game.run_quiz()



