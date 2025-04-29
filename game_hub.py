import random

# ----------------- Define the Quiz Game -----------------
def quiz_game():
    print("\n🎯 Welcome to the Quiz Game!")
    playing = input("Do you want to play? (yes/no): ").lower()
    if playing != "yes":
        return

    score = 0
    questions = [
        ("What is the capital of France?", "paris"),
        ("What does CPU stand for?", "central processing unit"),
        ("What does RAM stand for?", "random access memory"),
        ("What does ROM stand for?", "read only memory"),
        ("Which planet is known as the Red Planet?", "mars"),
        ("What is H2O commonly known as?", "water"),
        ("Who wrote 'Harry Potter'?", "j.k. rowling")
    ]

    for q, a in questions:
        answer = input(q + " ").lower().strip()
        if answer == a:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was {a.title()}.\n")

    print("="*50)
    print(f"🎯 You got {score} out of {len(questions)} questions correct!")
    percentage = (score / len(questions)) * 100
    print(f"📈 Your score: {percentage:.2f}%")
    print("="*50)

    if percentage == 100:
        print("🏆 Perfect! You're a genius!")
    elif percentage >= 70:
        print("👏 Great job! You really know your stuff!")
    elif percentage >= 50:
        print("👍 Not bad! Keep practicing!")
    else:
        print("😅 Better luck next time. Keep learning!")

    print("Thanks for playing! 🎮\n")

# ----------------- Define the Number Guessing Game -----------------
def number_guessing_game():
    print("="*50)
    print("🎯 Welcome to the Number Guessing Game!")
    print("="*50)

    top_of_range = input("🔢 Type the maximum number for the guessing range: ")
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        if top_of_range <= 0:
            print("⚠️ Please type a number larger than 0 next time.")
            return
    else:
        print("⚠️ Please type a valid number next time.")
        return

    random_num = random.randint(1, top_of_range)
    attempts = 0

    while True:
        user_guess = input("🤔 Make a guess or type 'QQ' to quit: ")

        if user_guess.upper() == "QQ":
            print("👋 You exited the game. See you next time!")
            break

        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("⚠️ Please type a valid number.")
            continue

        attempts += 1

        if user_guess == random_num:
            print(f"🎉 Congratulations! You guessed the number in {attempts} tries! 🏆")
            break
        elif user_guess > random_num:
            print("📉 Too high! Try a smaller number.")
        else:
            print("📈 Too low! Try a bigger number.")

    print("Thanks for playing! 🎮\n")

# ----------------- Define the Rock Paper Scissors Game -----------------
def rock_paper_scissors_game():
    user_wins = 0
    cpu_wins = 0
    options = ["rock", "paper", "scissors"]

    print("="*50)
    print("🪨📜✂️ Welcome to Rock, Paper, Scissors!")
    print("="*50)

    while True:
        user_input = input("\n👉 Type Rock/Paper/Scissors or Q to quit: ").lower()

        if user_input == "q":
            print("\n👋 Exiting game...")
            break

        if user_input not in options:
            print("⚠️ Invalid option! Please choose Rock, Paper, or Scissors.")
            continue

        cpu_pick = random.choice(options)
        print(f"🤖 CPU picked {cpu_pick.capitalize()}.")

        if user_input == cpu_pick:
            print("🤝 It's a tie!")
        elif (user_input == "rock" and cpu_pick == "scissors") or \
             (user_input == "paper" and cpu_pick == "rock") or \
             (user_input == "scissors" and cpu_pick == "paper"):
            print("🎉 You won this round!")
            user_wins += 1
        else:
            print("💻 CPU won this round!")
            cpu_wins += 1

    print("\n🏁 Final Results:")
    print(f"🏆 You won {user_wins} times.")
    print(f"🤖 CPU won {cpu_wins} times.")
    print("Thanks for playing! 🎮\n")

# ----------------- Define the Adventure Game -----------------
def adventure_game():
    name = input("What is your name? ")
    print(f"Welcome to the adventure, {name}! 🚀 Let's get you to school... if you survive 😎.")

    answer = input("You step outside your house. Do you go 'left' towards the woods 🌲 or 'right' towards the busy road 🚗? ").lower()

    if answer == "left":
        print("You bravely walk into the woods... it's spooky! 👻")
        answer = input("You see a river 🏞️. Do you 'swim' across or 'build' a raft? ").lower()

        if answer == "swim":
            print("The river was too strong! You got swept away... 😵 Game Over!")
        elif answer == "build":
            print("Smart move! You built a raft and crossed safely. 🛶")
            answer = input("Ahead, you see a cave 🕳️. Enter the 'cave' or go 'around' it? ").lower()

            if answer == "cave":
                print("Inside the cave you find a magic tunnel that teleports you straight to school! ✨🏫 You Win!")
            elif answer == "around":
                print("You got lost in the woods and ended up back home... 😅 Try again!")
            else:
                print("Invalid choice. You tripped and went home crying. 😭")
        else:
            print("Invalid choice. You stood by the river until nightfall... and a bear found you. 🐻 Game Over!")

    elif answer == "right":
        print("You walk towards the busy road, cars zooming past! 🚗💨")
        answer = input("Do you 'wait' for the pedestrian light 🚦 or 'run' across quickly? ").lower()

        if answer == "wait":
            print("You waited responsibly and crossed safely! 👏")
            answer = input("You see an ice cream truck 🍦. Buy some 'icecream' or keep 'walking' to school? ").lower()

            if answer == "icecream":
                print("The ice cream man was your school principal! 🍦🎓 Bonus points for being cool. You reach school on time!")
            elif answer == "walking":
                print("You march like a champion straight into school! 🏆 Good job!")
            else:
                print("You got distracted and missed school completely. 🤦‍♂️")
        elif answer == "run":
            print("You tried to run... but tripped and landed in a bush. 🥴 Game Over!")
        else:
            print("Invalid choice. You froze and missed school. 🥶")
    else:
        print("Confused, you just stayed home and played video games all day. 🎮 Try again!")

    print(f"\nThanks for playing, {name}! 🎉\n")

# ----------------- Main Menu -----------------
def main_menu():
    while True:
        print("________________________________________")
        print("🎮 Welcome to the Game Hub!")
        print("Please select a game to play:")
        print("1. Quiz Game")
        print("2. Number Guessing Game")
        print("3. Rock Paper Scissors")
        print("4. Adventure Story Game")
        print("5. Quit")
        print("________________________________________")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            quiz_game()
        elif choice == "2":
            number_guessing_game()
        elif choice == "3":
            rock_paper_scissors_game()
        elif choice == "4":
            adventure_game()
        elif choice == "5":
            print("Thanks for playing! Goodbye! 🚀")
            break
        else:
            print("Invalid choice. Please select a valid number (1-5).\n")

# Run the main menu
main_menu()
