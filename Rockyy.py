import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

def play_game(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    user_label.config(text="You chose:")
    computer_label.config(text="Computer chose:")

    user_icon.config(image=gif_icons[user_choice])
    computer_icon.config(image=gif_icons[computer_choice])

    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=result)

    if result == "You win!":
        show_party_animation()

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"


root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Load GIFs
rock_gif = Image.open("rock.png")
paper_gif = Image.open("paper.png")
scissors_gif = Image.open("scissor.png")


gif_icons = {
    "rock": ImageTk.PhotoImage(rock_gif),
    "paper": ImageTk.PhotoImage(paper_gif),
    "scissors": ImageTk.PhotoImage(scissors_gif)
}

# Create GUI elements
user_label = tk.Label(root, text="You chose:", font=("Helvetica", 20))
user_label.pack()

user_icon = tk.Label(root, image=None)
user_icon.pack()

vs_label = tk.Label(root, text="VS", font=("Helvetica", 20))
vs_label.pack()

computer_label = tk.Label(root, text="Computer chose:", font=("Helvetica", 20))
computer_label.pack()

computer_icon = tk.Label(root, image=None)
computer_icon.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 24))
result_label.pack()

rock_button = tk.Button(root, text="Rock", command=lambda: play_game("rock"), font=("Helvetica", 18))
rock_button.pack(side=tk.LEFT, padx=20, pady=10)

paper_button = tk.Button(root, text="Paper", command=lambda: play_game("paper"), font=("Helvetica", 18))
paper_button.pack(side=tk.LEFT, padx=20, pady=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("scissors"), font=("Helvetica", 18))
scissors_button.pack(side=tk.LEFT, padx=20, pady=10)

root.mainloop()
