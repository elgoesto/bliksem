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

# Function for the implementation of a Breath First Search.
def BFS(car, maxmoves):

    startboard = fun.SaveBoard(cc.Board.board)
    totcars = list(range(0, cc.TOTAL_CARS))
    for i in range(maxmoves ):
        print("amount of moves currently on:", i)
        for move in itertools.product(totcars, repeat = i + 1):
            move = list(move)
            for auto in move:
                if car[auto].move(-1):
                    car[auto].move(-1)
                elif car[auto].move(1):
                    car[auto].move(1)
            if cc.check():
                print("you won in", i + 1, "moves")
                print("winning moves:", move)
                break
            cc.Board.board = copy.copy(startboard)
