import random
import copy
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib import colors
import itertools
import carclass as cc
from statistics import mean
import functies as fun


# Function to pick a random direction, left/right or up/down.
def dirry():
    d = random.randint(1, 2)
    if d == 2:
        d = -1
    return d


# Function for a random algorithm.
def randomize(cars, RANDOM_CARS, TOTAL_CARS, dontmove = -1):
    score = 0
    # As long as the game is not won, keeping moving cars.
    while (cc.check() == False):
        # Check which cars can move in the current state of the board
        # except for the car you moved one move before.
        moves = fun.possible_moves(cars, dontmove)
        # Pick a car from moves and move it in a random positition.
        r = random.randint(0, (len(moves) - 1))
        d = dirry()

        # Keep moving the choosen car as far as possible.
        while(cars[moves[r]].move(d) == True):
            cars[moves[r]].move(d)

        score += 1
        dontmove = moves[r]
        moves = []

    print(cc.Board.board)
    print("You Won")
    print ("with " , score , " moves.")
    fun.visualise(cc.Board.board, cc.TOTAL_CARS, cc.RANDOM_CARS)

# Keep repeating the random function as above, and append the scores to a list.
def random_two(cars, RANDOM_CARS, TOTAL_CARS, dontmove = -1):
    score_list = []
    startboard = np.copy(cc.Board.board)
    for i in range(11):
        for i in range(2000):
            score = 0
            while (cc.check() == False):
                moves = fun.possible_moves(cars, dontmove)
                r = random.randint(0, (len(moves) - 1))
                d = dirry()
                while(cars[moves[r]].move(d) == True):
                    cars[moves[r]].move(d)
                score += 1
                dontmove = moves[r]
                moves = []
            cc.Board.board = copy.copy(startboard)
            score_list.append(score)
        print(min(score_list))
        print(mean(score_list))
