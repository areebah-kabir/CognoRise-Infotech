import random

def play_rps():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    computer_choice = random.choice(choices)
    
    if user_choice == computer_choice:
        return f"Both chose {user_choice}. It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return f"You chose {user_choice}, computer chose {computer_choice}. You win!"
    else:
        return f"You chose {user_choice}, computer chose {computer_choice}. You lose."

print(play_rps())
