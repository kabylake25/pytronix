import random


class Dice:
    def roll(self):
        print((random.randint(1, 6), random.randint(1, 6)))


dice = Dice()
dice.roll()
