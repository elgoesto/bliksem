import carclass as cc
import random
import copy
import numpy as np
import time
from statistics import mean

# part of the ramdom algorithm, this picks a ramdom direction.
def dirry():
    d = random.randint(1,2)
    if d == 2:
        d = -1
    return d

def random_two(cars, RANDOM_CARS):

    # Create a list to store all of the scores, create a copy of the startboard.
    score_list = []
    startboard = copy.copy(cc.Board.board)

    for i in range(20):
        for i in range(5000):
            score = 0

            # As long as the game is not won, keep moving cars.
            while (cc.check() == False):
                r = random.randint(0, RANDOM_CARS)
                d = dirry()
                while(cars[r].move(d) == True):
                    cars[r].move(d)
                score += 1

            # Set the board to it's startposition and append the score to the list.
            cc.Board.board = copy.copy(startboard)
            score_list.append(score)

        #print(score_list)
        print(min(score_list))
        print(mean(score_list))
