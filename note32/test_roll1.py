import random


def roll():
    return random.randint(1, 6)


i = 1
isWinner = False
while i <= 3:
    rollResult = roll()
    print("roll result is {!s}".format(rollResult))
    if(rollResult == 6):
        isWinner = True
        break
    i += 1
if isWinner:
    print("you are a winner")
else:
    print('you are a loser')