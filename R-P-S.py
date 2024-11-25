import random

user_won = 0
cpu_won = 0
choice = ["rock", "paper", "scissors"]

def play_round():
    user_input = input("Enter rock/paper/scissors or q to quit the game: ").lower()
    if user_input == "q":
        return False

    if user_input not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please try again.")
        return True

    random_num = random.randint(0, 2)
    cpu_choice = choice[random_num]
    print("CPU picked", cpu_choice)

    if user_input == "rock" and cpu_choice == "scissors":
        print("You won!🥳")
        return "player"
    elif user_input == "paper" and cpu_choice == "rock":
        print("You won!🥳")
        return "player"
    elif user_input == "scissors" and cpu_choice == "paper":
        print("You won!🥳")
        return "player"
    elif user_input == cpu_choice:
        print("It's a Tie")
        return "tie"
    else:
        print("You lost😓")
        return "cpu"

while True:
    result = play_round()
    if result == "player":
        user_won += 1
    elif result == "cpu":
        cpu_won += 1

    if not result:
        break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("\nGAME OVER")
print("You won", user_won, "times")
print("CPU won", cpu_won, "times")