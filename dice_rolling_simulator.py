import random

while True:

    roll_dice = input("would you like to roll the dice? (y/n): ").lower()

    while roll_dice != 'y' and roll_dice != 'n':
        roll_dice = input("please enter y or n: ")

    if roll_dice == 'y':
        print(random.randrange(1, 7))
    elif roll_dice == 'n':
        print("Exit")
        break
