import random

# Choices
choices = ["rock", "paper", "scissors"]

# Take input from the user
user_choice = input("Enter rock, paper, or scissors: ").lower()

# Computer makes a random choice
computer_choice = random.choice(choices)

print(f"\nYou chose: {user_choice}")
print(f"Computer chose: {computer_choice}\n")

# Decide the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("🎉 You win!")
else:
    print("💻 Computer wins!")
