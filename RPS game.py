import random
print("NOTE- r=rock ; s=stone ; p=paper")
def get_user_choice():
    while True:
        user_choice = input("Enter your choice (r, p, or s): ").lower()
        # r=rock ; s=stone ; p=paper;
        if user_choice in ["r", "p", "s"]:
            return user_choice
        else:
            print("Invalid choice. Please choose r, p, or s.")

def get_computer_choice():
    return random.choice(["r", "p", "s"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "r" and computer_choice == "s")
        or (user_choice == "p" and computer_choice == "r")
        or (user_choice == "s" and computer_choice == "p")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_score = 0
    computer_score = 0
    rounds = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        print(f"You chose {user_choice}. Computer chose {computer_choice}. {result}")

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        rounds += 1

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            break

    print(f"Game Over! You played {rounds} rounds.")
    print(f"Your score: {user_score}")
    print(f"Computer's score: {computer_score}")

if __name__ == "__main__":
    main()
