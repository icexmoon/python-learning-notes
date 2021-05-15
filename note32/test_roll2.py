import random


def roll():
    return random.randint(1, 6)


i = 1
while i <= 3:
    rollResult = roll()
    print("rull result is {!s}".format(rollResult))
    if(rollResult == 6):
        print('you are a winner')
        break
    i += 1
else:
    print("you are a loser")