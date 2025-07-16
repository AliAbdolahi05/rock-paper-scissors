import random

# ============================================================
#  ██████╗  ██████╗  ██████╗██╗  ██╗    ██████╗  █████╗ ███████╗
#  ██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝    ██╔══██╗██╔══██╗██╔════╝
#  ██████╔╝██║   ██║██║     █████╔╝     ██████╔╝███████║███████╗
#  ██╔═══╝ ██║   ██║██║     ██╔═██╗     ██╔══██╗██╔══██║╚════██║
#  ██║     ╚██████╔╝╚██████╗██║  ██╗    ██║  ██║██║  ██║███████║
#  ╚═╝      ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
# ============================================================
# Rock, Paper, Scissors Game - PRO EDITION
# Author: Ali Abdollahi
# Description:
#   Play an epic match of "Rock, Paper, Scissors" against the computer!
#   First to reach 3 points is the champion.
#   Enjoy clean code, pro comments, and a fun experience!
# ============================================================

options = ("ROCK", "PAPER", "SCISSORS")  # Game options

human_score = 0  # Human player score
robot_score = 0  # Robot player score

# =========================
#  Decision Functions
# =========================


def user_choice_rock():
    """
    User chooses 'ROCK'.
    Compares with robot's choice and updates scores.
    """
    global human_score, robot_score
    if robot_choice == "ROCK":
        print(f"🤖 Robot: {robot_choice} ---> Draw! 🤝")
    elif robot_choice == "SCISSORS":
        print(f"🤖 Robot: {robot_choice} ---> Human wins this round! 🏆")
        human_score += 1
    elif robot_choice == "PAPER":
        print(f"🤖 Robot: {robot_choice} ---> Robot wins this round! 🤖")
        robot_score += 1


def user_choice_paper():
    """
    User chooses 'PAPER'.
    Compares with robot's choice and updates scores.
    """
    global human_score, robot_score
    if robot_choice == "ROCK":
        print(f"🤖 Robot: {robot_choice} ---> Human wins this round! 🏆")
        human_score += 1
    elif robot_choice == "SCISSORS":
        print(f"🤖 Robot: {robot_choice} ---> Robot wins this round! 🤖")
        robot_score += 1
    elif robot_choice == "PAPER":
        print(f"🤖 Robot: {robot_choice} ---> Draw! 🤝")


def user_choice_scissors():
    """
    User chooses 'SCISSORS'.
    Compares with robot's choice and updates scores.
    """
    global human_score, robot_score
    if robot_choice == "ROCK":
        print(f"🤖 Robot: {robot_choice} ---> Robot wins this round! 🤖")
        robot_score += 1
    elif robot_choice == "SCISSORS":
        print(f"🤖 Robot: {robot_choice} ---> Draw! 🤝")
    elif robot_choice == "PAPER":
        print(f"🤖 Robot: {robot_choice} ---> Human wins this round! 🏆")
        human_score += 1


# =========================
#  Main Game Loop
# =========================
while True:
    user_input = input("Your choice? (ROCK, PAPER, SCISSORS): ").upper()
    robot_choice = random.choice(options)

    if human_score != 3 and robot_score != 3:
        if user_input == "ROCK":
            user_choice_rock()
            print(f"Score: Human {human_score} - Robot {robot_score}\n")
        elif user_input == "PAPER":
            user_choice_paper()
            print(f"Score: Human {human_score} - Robot {robot_score}\n")
        elif user_input == "SCISSORS":
            user_choice_scissors()
            print(f"Score: Human {human_score} - Robot {robot_score}\n")
        else:
            print("❌ Invalid input! Please choose ROCK, PAPER, or SCISSORS.\n")
    else:
        print("="*40)
        if human_score > robot_score:
            print("🏆 Human player is the WINNER! Congratulations! 🏆")
        else:
            print("🤖 Robot player is the WINNER! Better luck next time! 🤖")
        print("="*40)
        break

print(f"Final Score -> Human: {human_score} | Robot: {robot_score}")
