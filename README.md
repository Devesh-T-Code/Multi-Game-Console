# Interactive Fun Suite: Rock, Flip, and Bat!
#### Video Demo:  <https://youtu.be/JgjAvvqR140>
#### Description:

Overview:

This project is a Python-based console game application that combines three popular mini-games into one program:

    1.)Rock-Paper-Scissors
    2.)Heads or Tails
    3.)Hand Cricket
The user interacts with the program via a text-based interface, selecting games, making decisions, and competing against the computer in an engaging and fun manner.

Key Features

Multiple Games in One Console:
The program offers three classic games, each with its own set of rules and outcomes, providing variety and replayability.

Randomized Computer Decisions:
Leveraging the random module, the program ensures fairness by simulating unbiased computer guesses and decisions.

Dynamic Gameplay:
Real-time score tracking, multiple game rounds, and interactive player decisions keep users engaged.

Replay Option:
After completing any game, users can choose to replay the same game, switch to another, or exit the program gracefully.

Error Handling:
The program includes robust input validation and gracefully exits on invalid inputs with a message.

Games Overview
    1. Rock-Paper-Scissors
        Objective: Score 3 points before the computer.
        Rules:
            1.)Rock beats Scissors.
            2.)Scissors beats Paper.
            3.)Paper beats Rock.
        Gameplay:
            1.)Players choose Rock, Paper, or Scissors (1, 2, or 3).
            2.)The computer randomly selects its choice.
            3.)Results are announced after each round.
            4.)The game continues until one player scores 3 points.
    Outcome: Victory is declared based on scores.

    2. Heads or Tails
        Objective: Guess the outcome of a coin flip.
        Rules:
            1.)Player chooses Head or Tail.
            2.)The computer flips a coin (random choice of Head or Tail).
            3.)If the player's guess matches the result, they win.
        Gameplay:
            1.)The user selects Head (1) or Tail (2).
            2.)The computer simulates a coin flip and reveals the result.
    Outcome: Success or failure is displayed immediately.

    3. Hand Cricket
        Objective: Score more runs than the computer.
        Rules:
            1.)The game starts with a toss (Odd/Even selection).
            2.)The winner chooses to bat or bowl first.
            3.)Players score runs (1 to 6), and the inning ends if runs match.
            4.)The second player attempts to chase the target set by the first.
        Gameplay:
            1.)Toss determines the batting or bowling order.
            2.)Runs are scored by entering values (1–6), while the computer makes simultaneous guesses.
            3.)If the runs match, the inning ends.
    Outcome: The winner is determined based on the target and score comparison.

Code Structure:

    Main Functionality:
T       1.)he main() function drives the program, displaying the game menu and handling user choices.
        2.)It utilizes the match-case construct to route users to their selected game.
    Game Logic Functions:
        1.)Each game has a dedicated function:
                rock_paper_scissor()
                head_tail()
                hand_cricket()
            These functions encapsulate game rules, decision-making, and outcomes.
        2.)Helper Functions
                get_game(): Displays the menu and captures the user's choice.
                random_computer_guess(): Randomly generates the computer's guess using the random module.
                user_run(): Captures and validates user input for numeric decisions.
                toss_result(): Determines the outcome of the toss in Hand Cricket.
                bat(), bowl(), result(), and target(): Handle Hand Cricket-specific gameplay.

    Input Validation and Error Handling:
        1.)The program uses try-except blocks to prevent crashes due to invalid inputs.
        2.)Exits gracefully with an error message if an invalid choice is detected.

Technologies Used:
    Programming Language: Python
    Modules: random, sys

