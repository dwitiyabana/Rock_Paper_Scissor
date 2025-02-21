import random  # Import random module for computer choice

# Available choices
choices = ["rock", "paper", "scissors"]

while True:
    print("\n--- ROCK, PAPER, SCISSORS GAME ---")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'exit' to quit the game.")

    # Get user input
    user_choice = input("Your choice: ").lower()

    if user_choice == "exit":
        print("Goodbye! Thanks for playing. ")
        break  # Exit the loop

    if user_choice not in choices:
        print("❌ Invalid choice! Please choose rock, paper, or scissors.")
        continue  # Restart the loop

    # Computer's random choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    # Determine the winner
    if user_choice == computer_choice:
        print(" It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("🎉 You win!")
    else:
        print(" You lose!")