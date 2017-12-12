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


# part of the ramdom algorithm, this picks a random direction.
def dirry():
    d = random.randint(1,2)
    if d == 2:
        d = -1
    return d


# This is the ramdom algorithm.
def randomize(cars, RANDOM_CARS, TOTAL_CARS, dontmove = -1):
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

    print(cc.Board.board)
    print("You Won")
    print ("with " , score , " moves.")
    fun.visualise(cc.Board.board, cc.TOTAL_CARS)

# Random function Two, needs to be optimized. NOT DONE YET.
def random_two(cars, RANDOM_CARS, TOTAL_CARS, dontmove = -1):
    score_list = []
    startboard = np.copy(cc.Board.board)
    for i in range(9):
        for i in range(5):
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
            #print(cc.Board.board)
            #print("You Won")
            #print ("with " , score , " moves.")
            cc.Board.board = copy.copy(startboard)
            score_list.append(score)
        # print(score_list)
        print(min(score_list))
        print(mean(score_list))
