import tkinter as tk
from tkinter import messagebox
import random
import os
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

def load_image(file_path, size=(103, 150)):
    image = Image.open(file_path)
    image = image.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(image)

rock_img_path = r"D:\college\internship\CodSoft\tasks\rock paper scissor\rock.png"
paper_img_path = r"D:\college\internship\CodSoft\tasks\rock paper scissor\paper.png"
scissors_img_path = r"D:\college\internship\CodSoft\tasks\rock paper scissor\scissors.png"

try:
    rock_img = load_image(rock_img_path)
    paper_img = load_image(paper_img_path)
    scissors_img = load_image(scissors_img_path)
except Exception as e:
    print(e)
    root.destroy()  
    exit()

user_score = 0
computer_score = 0

def update_scores():
    score_label.config(text=f"Score -> You: {user_score} | Computer: {computer_score}")

def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1
    return result

def play(user_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(user_choice, computer_choice)
    
    user_choice_img = load_image(globals()[f"{user_choice}_img_path"])
    computer_choice_img = load_image(globals()[f"{computer_choice}_img_path"])
    
    user_choice_label.config(image=user_choice_img)
    user_choice_label.image = user_choice_img  
    
    computer_choice_label.config(image=computer_choice_img)
    computer_choice_label.image = computer_choice_img  
    
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    update_scores()

def quit_game():
    root.quit()

frame = tk.Frame(root)
frame.pack(pady=20)

rock_button = tk.Button(frame, image=rock_img, command=lambda: play('rock'))
rock_button.grid(row=0, column=0, padx=10)
paper_button = tk.Button(frame, image=paper_img, command=lambda: play('paper'))
paper_button.grid(row=0, column=1, padx=10)
scissors_button = tk.Button(frame, image=scissors_img, command=lambda: play('scissors'))
scissors_button.grid(row=0, column=2, padx=10)

user_choice_label = tk.Label(root)
user_choice_label.pack(side=tk.LEFT, padx=20)

computer_choice_label = tk.Label(root)
computer_choice_label.pack(side=tk.RIGHT, padx=20)

result_label = tk.Label(root, text="", font=('Helvetica', 14))
result_label.pack(pady=20)

score_label = tk.Label(root, text=f"Score -> You: {user_score} | Computer: {computer_score}", font=('Helvetica', 14))
score_label.pack(pady=20)

quit_button = tk.Button(root, text="Quit", command=quit_game)
quit_button.pack(pady=20)

root.mainloop()
