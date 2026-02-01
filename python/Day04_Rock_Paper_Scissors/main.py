# Rock Papper Scissors
import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_result(player, computer):
    if player == computer:
        return "draw"
    
    if (
        (player == "rock" and computer == "scissors") or
        (player == "scissors" and computer == "paper") or
        (player == "paper" and computer == "rock")
    ):
        return "win"
    else:
        return "lose"


def play_game():
    player_score = 0
    computer_score = 0

    print("🎮 Welcome to Rock Paper Scissors Game 🎮")
    while True:
        print("\nChoose One: ")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")

        choice = input("Enter your choice(1-4): ").strip()

        if choice == "4":
            print("\n 👋 Thanks for playing")   
            print(f"final score -> You: {player_score} | Computer: {computer_score}")
            break

        choice_map = {
            "1" : "rock",
            "2" : "paper",
            "3" : "scissors"
        } 

        if choice not in choice_map:
            print("❌ Invalid choice, try again.")
            continue

        player_choice = choice_map[choice]
        computer_choice = get_computer_choice()

        print(f"👨‍🦱 You chose {player_choice}")
        print(f"🖥️ Computer chose {computer_choice}")

        result = get_result(player_choice, computer_choice)

        if result == "win":
            print("🎉 You win!")
            player_score += 1
        elif result == "lose":
            print("😢 Computer wins!")
            computer_score += 1
        else:
            print("🤝 It's a draw!")

        print(f"📊 Score → You: {player_score} | Computer: {computer_score}")


if __name__ == "__main__":
    play_game()