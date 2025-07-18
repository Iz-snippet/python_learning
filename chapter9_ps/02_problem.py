# The game() function in a program lets a user play a game and returns the score as an integer. 
# You need to read a file hiscore.txt, which is either blank or contains the previous hi-score. 
# You need to write a program to update the hi-score whenever game() breaks the hi-score.

import random

def game():
    print("You are playing the game...")

    score = random.randint(1, 64)

    # Fetch the hiscore
    try:
        with open("hiscore.txt") as f:
            hiscore = f.read()
            if hiscore == "":
                hiscore = 0
            else:
                hiscore = int(hiscore)
    except FileNotFoundError:
        hiscore = 0

    print(f"Your score: {score}")

    # Update if current score is greater
    if score > hiscore:
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
        print("🎉 New High Score!")
    else:
        print("Better luck next time!")

    return score

game()

