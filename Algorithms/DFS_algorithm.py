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
import sys

def DFS(cars, MAX_MOVE, dontmove = -1, movelist = []):
    if cc.check() == True:
        print(cc.Board.board)
        sys.exit("you won")
    count = MAX_MOVE - 1
    if count > 0:
        moves = fun.possible_moves(cars, dontmove)
        for car in moves:
            if cars[car].move(1):
                while bool(cars[car].move(1)) == True:
                    cars[car].move(1)
                DFS(cars, count, car)
                while bool(cars[car].move(-1)) == True:
                    cars[car].move(-1)
            else:
                while bool(cars[car].move(-1)) == True:
                    cars[car].move(-1)
                DFS(cars, count, car)
                while bool(cars[car].move(1)) == True:
                    cars[car].move(1)
