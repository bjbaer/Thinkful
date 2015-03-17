import random
import matplotlib.pyplot as plt
import collections
class Dice(object):
    def __init__(self, sides = 6):
        self.sides = sides
        last_result = None

    def roll(self):
        self.last_result = result = random.randint(1, self.sides)  + random.randint(1, self.sides)
        return result

def roll_dice(dice):
	minres = []
	maxres = []
	for die in xrange(dice):
		trial = []
		for i in xrange(10):
			trial.append(Dice(6).roll())
		minres.append(min(trial))
		maxres.append(max(trial))
	print collections.Counter(minres)
	print collections.Counter(maxres)

def main():
    dice = 100
    roll_dice(dice)


if __name__ == '__main__':
    main()

