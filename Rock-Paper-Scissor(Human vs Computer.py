import random

print("Welcome To Rock Paper Scissor \n"
      "Game Rules are: \n"
      "Rock + Paper --> Paper \n"
      "Rock + Scissor --> Rock \n"
      "Paper + Scissor --> Scissor\n")

choices = {1: "Rock", 2: "Paper", 3: "Scissor"}

#checking Winning possibilites

def check_win(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissor") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissor" and computer_choice == "Paper"):
        return "You Win!"
    else:
        return "Computer Wins!"

#Main Game

def play_game():
    user_num = int(input("Choose:\n1. Rock\n2. Paper\n3. Scissor\nEnter choice: "))
    if user_num not in choices:
        print("Invalid choice! Please enter 1, 2, or 3.")
        return

    user_choice = choices[user_num]
    computer_choice = choices[random.randint(1, 3)]

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    print(check_win(user_choice, computer_choice))

# Loop to play multiple times
while True:
    play_game()
    again = input("\nDo you want to play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing! Goodbye 👋")
        break
