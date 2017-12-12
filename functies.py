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


# part of the ramdom algorithm, this picks a random direction.
def dirry():
    d = random.randint(1,2)
    if d == 2:
        d = -1
    return d


# This is the ramdom algorithm.
def randomize(cars, RANDOM_CARS, dontmove = -1):
    score = 0
    while (cc.check() == False):
        moves = possible_moves(cars, dontmove)
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

def visualise(board, TOTAL_CARS):
    # cmap = colors.ListedColormap(["white", "red", "blue", "green", "yellow"])
    color_lijst = ["white", "red"]
    color_overig = ["yellow", "pink", "orange", "blue", "green", "black", "brown", "magenta", "purple", "violet", "beige", "cyan"]
    for i in range(TOTAL_CARS-1):
        color_lijst.append(color_overig[i%len(color_overig)])
    print(color_lijst)

    cmap = colors.ListedColormap(color_lijst)

    bounds = []
    for i in range(TOTAL_CARS+2):
        bounds.append(i)
    print(bounds)

    fig, ax = plt.subplots()
    norm = colors.BoundaryNorm(bounds, cmap.N)
    ax.imshow(board, cmap=cmap, norm=norm)
    return plt.show()


# Function to make a copy of the startposition of the board.
def SaveBoard(board):
    startboard = copy.copy(cc.Board.board)
    return startboard

# Random function Two, needs to be optimized. NOT DONE YET.
def random_two(cars, RANDOM_CARS):
    score_list = []
    startboard = np.copy(cc.Board.board)
    for i in range(9):
        for i in range(5000):
            score = 0
            while (cc.check() == False):
                moves = possible_moves(cars, dontmove)
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

def possible_moves(cars, dontmove = -1):
    possible_moves = []
    for i in range (cc.TOTAL_CARS):
        if cars[i].possible_move() == True and i != dontmove:
            possible_moves.append(i)

    return possible_moves

def DFS(cars, MAX_MOVE, dontmove = -1, movelist = []):
    if cc.check() == True:
        print(cc.Board.board)
        sys.exit("you won")
    count = MAX_MOVE - 1
    if count > 0:
        moves = possible_moves(cars, dontmove)
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

# Function for the implementation of a Breath First Search.
def BFS(car, maxmoves):

    startboard = SaveBoard(cc.Board.board)
    totcars = list(range(0, cc.TOTAL_CARS))
    for i in range(maxmoves - 1):
        movespace = list(itertools.product(totcars, repeat = i + 1))
        print("amount of moves currently on:", i)
        for move in movespace:
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
