import random

def play_game(username):
    while True:
        print("\nSelect Difficulty: 1-Easy | 2-Medium | 3-Hard")
        level = input("Enter choice: ")

        if level == "1":
            low, high, MAX_ATTEMPTS = 1, 10, None
            break
        elif level == "2":
            low, high, MAX_ATTEMPTS = 1, 50, 10
            break
        elif level == "3":
            low, high, MAX_ATTEMPTS = 1, 100, 7
            break
        else:
            print("❌ Invalid Choice")
        
    rand_guess = random.randint(low, high)
    attempts = 0

    print("🎮 Game Started!")

    while True:
        try:
            user_input = int(input(f"Guess the Number ({low} to {high}): "))
        except ValueError:
            print("❌ Please Enter a valid  Number.")
            continue

        if user_input < low or user_input > high:
            print(f"⚠️  Guess must be between {low} and {high}.")
            continue

        attempts += 1

        if user_input == rand_guess:
            print(f"✅ {username}, you guessed it in {attempts} attempts!")
            return
        elif user_input < rand_guess:
            low = user_input 
            print(f"Low 📉 guess")
        elif user_input > rand_guess:
            high = user_input
            print(f"High 📈 guess")

        if MAX_ATTEMPTS is not None and attempts >= MAX_ATTEMPTS:
            print(f"❌ Sorry {username}, Attempts over!")
            print(f"🎯 The correct number was {rand_guess}")
            return
        
username = input("\nEnter your name: ").strip().title()
print(f"👋 Welcome, {username}!")

while True:
    play_game(username)

    choice = input("\nPlay again? (c = continue / q = quit): ").strip().lower()

    if choice == "c":
        continue
    elif choice == "q":
        print(f"👋 Thanks for playing, {username}!")
        break
    else:
        print("❌ Invalid choice. Game exiting.")
        break