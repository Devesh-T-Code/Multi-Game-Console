import random
import sys


def main():
    while True:
        game = get_game()
        match game:
            case "1":
                again = rock_paper_scissor()
            case "2":
                again = head_tail()
            case "3":
                again = hand_cricket()
            case _:
                raise ValueError
        if again.lower() not in ["y", "yes"]:
            sys.exit(
                "\n---------------------->Thank You for playing😊<----------------------\n"
            )


def get_game():
    games = ["1.Rock Paper Scissor🪨", "2.Heads or Tails🪙", "3.Hand Cricket🏏"]
    print("\nPick one game(1, 2 or 3)")
    for game in games:
        print(game)
    return input("Choose😊:").strip()


def rock_paper_scissor():
    choices = ["Rock🪨", "Paper📄", "Scissor✂️"]
    score = 0
    computer_score = 0
    round = 0
    print(
        """
          Rules of the game:
          1.) You are to select Rock🪨, Paper📄 or Scissor✂️  by selecting 1, 2 or 3
          2.) Rock🪨  against Rock🪨       ---> Draw
              Rock🪨  against Paper📄      ---> Paper📄  wins
              Rock🪨  against Scissor✂️    ---> Rock🪨  wins
              Paper📄  against Paper📄     ---> Draw
              Paper📄  against Scissor✂️   ---> Scissor✂️  wins
              Scissor✂️  against Scissor✂️ ---> Draw
           3.) You and the computer will simultaneously make a guess.
           4.) The first to score 3 points will win!!!
          """
    )
    while score < 3 and computer_score < 3:
        round += 1
        try:
            print(
                f"\n\nRound:{round} Your Score:{score} Computer Score:{computer_score}"
            )
            guess = int(
                input("1.Rock🪨  2.Paper📄 3.Scissor✂️  (Select 1, 2 or 3):").strip()
            )
            guess = choices[guess - 1]
        except (ValueError, IndexError):
            sys.exit("Invalid Choice")
        computer_guess = random_computer_guess(choices)
        print(f"{guess}  vs {computer_guess}")
        if guess == "Rock🪨" and computer_guess == "Rock🪨":
            print("Clash--No point! Try again")
        elif guess == "Rock🪨" and computer_guess == "Paper📄":
            computer_score += 1
        elif guess == "Rock🪨" and computer_guess == "Scissor✂️":
            score += 1
        elif guess == "Paper📄" and computer_guess == "Rock🪨":
            score += 1
        elif guess == "Paper📄" and computer_guess == "Paper📄":
            print("Clash--No point! Try again")
        elif guess == "Paper📄" and computer_guess == "Scissor✂️":
            computer_score += 1
        elif guess == "Scissor✂️" and computer_guess == "Rock🪨":
            computer_score += 1
        elif guess == "Scissor✂️" and computer_guess == "Paper📄":
            score += 1
        elif guess == "Scissor✂️" and computer_guess == "Scissor✂️":
            print("Clash--No point! Try again")
    if score > computer_score:
        print(f"Your score: {score}, Computer score: {computer_score}\n You win🏆!!!")
    else:
        print(
            f"Your score: {score}, Computer score: {computer_score}\n Good game! Better luck next time😉"
        )
    return input("Do you wish to play again?(yes or no): ")


def head_tail():
    choices = ["Head", "Tail"]
    print(
        """
          Rules of the game:
          1.) You are to select Head or Tail  by selecting 1 or 2
          2.) Computer will make a flip(random) to make a guess.
          3.) If your selection is correct, You win!!!
          """
    )
    try:
        guess = int(input("Pick a side\n1.Head  2.Tail (Select 1 or 2):").strip())
        guess = choices[guess - 1]
    except (ValueError, IndexError):
        sys.exit("Invalid Choice")
    computer_guess = random_computer_guess(choices)
    print(f"\nYour guess:{guess}---Computer guess:{computer_guess}")
    if guess == computer_guess:
        print("You guessed right!!!🟢")
    else:
        print("Better luck next time⭕")
    return input("Do you wish to play again?(yes or no): ").strip()


def hand_cricket():
    choices = range(1, 7)
    print(
        """
          Rules of the game:
          1.) You are to select Odd or Even  by selecting 1 or 2
          2.) You are to hit and score runs from 1 to 6 by selecting any number from 1 to 6.
          3.) Computer also simultaneously hits a run
          4.) If the sum is reportedly \"Odd\" or \"Even\" as per your guess,
              You choose to bat or bowl ( By again selecting 1 or 2)
          5.) If your guess is wrong, computer gets the choice.
          6.) Then accordingly you and computer simlutaneously hit runs to score and if both runs match,
              the batter is out, and a target is set.
          7.) If the target is surpassed, the second player wins, or else the first batter wins.
          8.) The match can also be a draw if both of them scored the same runs!!!           
          """
    )
    toss_choices = ["Odd", "Even"]
    innings = ["Bat", "Bowl"]
    try:
        toss = int(input("Choose 1.Odd 2.Even (Select 1 or 2): ").strip())
        toss = toss_choices[toss - 1]
        print(f"You choose {toss}")
    except (ValueError, IndexError):
        sys.exit("Invalid Choice")
    run = user_run()
    computer_run = random_computer_guess(choices)
    print(
        f"\nComputer hit: {computer_run}\n {run} + {computer_run} is {toss_result(run, computer_run)}"
    )
    if toss == toss_result(run, computer_run):
        player_choice = int(input("\nPick 1.Bat 2.Bowl(Select 1 or 2): ").strip())
        try:
            player_choice = innings[player_choice - 1]
        except (ValueError, IndexError):
            sys.exit("Invalid Choice")
        if player_choice == "Bat":
            print(f"\nYou choose Batting")
            player_bat()

        if player_choice == "Bowl":
            print(f"\nYou choose Bowling")
            player_bowl()

    else:
        computer_choice = random_computer_guess(innings)
        print(f"Computer choose to {computer_choice}")
        if computer_choice == "Bat":
            print(f"\nYou're Bowling, Bring up the squad!!!")
            player_bowl()
        if computer_choice == "Bowl":
            print(f"\nIt's batting time, Send some smashers!!!")
            player_bat()
    return input("Do you wish to play again?(yes or no): ")


def player_bat():
    target = bat("user")
    print(f"Your final score: {target - 1}\nTarget: {target}\nNow it's time to bowl!!!")
    outcome = bowl(target, "user")
    if outcome == 1:
        print("Computer Won!!! Nice play!!")
    elif outcome == 2:
        print("You won!!!! Had a blast!")
    else:
        print("The Match is a Draw! Rematch?")


def player_bowl():
    target = bat("computer")
    print(
        f"Computer final score: {target - 1}\nTarget: {target}\nNow it's time to smash sixes!!!"
    )
    outcome = bowl(target, "computer")
    if outcome == 1:
        print("You Won!!! Great play!!")
    elif outcome == 2:
        print("Better Luck next time!!")
    else:
        print("The Match is a Draw! Rematch?")


def bat(player):
    choices = range(1, 7)
    run, computer_run = 0, 1
    score = 0
    while run != computer_run:
        run = user_run()
        computer_run = random_computer_guess(choices)
        print(f"Computer hit: {computer_run}")
        if run != computer_run:
            if player == "user":
                score += run
                print(f"Your Score: {score}")
            else:
                score += computer_run
                print(f"Computer Score: {score}")
    return target(score)


def bowl(target, player):
    choices = range(1, 7)
    run, computer_run = 0, 1
    score = 0
    flag = 0
    while run != computer_run and score < target:
        run = user_run()
        computer_run = random_computer_guess(choices)
        print(f"Computer hit: {computer_run}")
        if run != computer_run:
            if player == "user":
                score += computer_run
                print(f"Computer Score: {score} Target: {target}")
            else:
                score += run
                print(f"Your Score: {score} Target: {target}")
        elif run == computer_run and score == target:
            flag = 1
    return result(score, target, flag)


def result(score, target, flag = 0):
    if not flag:
        if score > target or score == target:
            return 1
        elif score < target:
            return 2
        else:
            return 0
    else:
        return 0


def target(score):
    return score + 1


def user_run():
    choices = range(1, 7)
    try:
        run = int(input("\nRun(Pick 1 to 6):").strip())
        run = choices[run - 1]
    except (ValueError, IndexError):
        sys.exit("Invalid Choice")
    return run


def random_computer_guess(choices):
    return random.choice(choices)


def toss_result(user, computer):
    if (user + computer) % 2 == 0:
        return "Even"
    else:
        return "Odd"


if __name__ == "__main__":
    main()
