# We are going to implement a random-number guessing game.
# This program will combine if-statements, main loops, and random number generation.
# We will discuss the design of this program in class. I will show a working version as a reference for what it should do.

#=======================
# TODO
# Implement this project in 2 phases.
#
# First make a guessing game that you can play once. Pseudocode:
#     Generate a new, random secret number between 0 and 100 each time the game runs.
#     Keep track of the number of guesses the player makes (starts at 0)
#     Implement a main loop
#         Have the player make a guess at what the number is
#         Add 1 to the guess counter
#         If their guess is correct, end the game
#         Otherwise, tell the player whether their guess was too low or too high.
#     At the end, print out the player's score.
#
# Second, add the ability to replay the game without restarting the script, as well as a few other commands we will talk about.
#     This will involve nesting the main loop from the original version inside another loop.
#     We will discuss how to organize the code to make it easier.
#     Additional commands include q to quit, r to restart, z to cheat and see the secret number, s to change the maximum secret to a different value than 100

import random

def main():
    pass

if __name__ == "__main__":
    main()