""" This module represents the testing framework used to
generate potential run scenarios for the framework"""

from random import random, randint

class Monster(object):
    """Monster class encapsulates the aggressiveness and
    color. The aggressiveness should not be accessed and
    as such its name has been mangled """

    def __init__(self, aggressive, color, label):
        """Initializes the monster"""
        self._aggressive = aggressive
        self.color = color
        self.label = label

    def action(self, should_attack):
        """Act on the monster"""
        if not should_attack:
            return 0
        if self._aggressive:
            return -1
        return 1

def monster_generator():
    """Provides a generator for monsters"""
    while True:
        color = randint(1, 100)
        if color <= 70:
            if random() <= 0.30:
                yield Monster(1, color, 'A')
            else:
                yield Monster(0, color, 'A')
        else:
            if random() <= 0.95:
                yield Monster(0, color, 'B')
            else:
                yield Monster(1, color, 'B')

def run_tests(hypothesis, trials=100):
    generator = monster_generator()

    score = 0.0
    max_score = 0.0

    for x in range(trials):
        monster = next(generator)

        if monster._aggressive == 0:
            max_score += 1

        guess = hypothesis.get_guess(monster)
        outcome = monster.action(True)
        hypothesis.update(monster, guess, outcome)

        score += outcome

    print('Maximum Score: ' + str(max_score))
    print('Score        : ' + str(score))
    print('Success Rate : ' + str(score / max_score))
    print('')



if __name__ == "__main__":
    monster_generator = monster_generator()

    for x in range(10):
        monster = monster_generator.next()
        print(x)
        print(monster.label)
        print(monster._aggressive)
        print(monster.color)
        print('')
