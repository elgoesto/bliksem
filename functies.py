import random
import copy
import numpy as np
import time
import matplotlib.pyplot as plt
import itertools
import test_carclass as cc
import board as bb




# part of the ramdom algorithm, this picks a ramdom direction.
def dirry():
    d = random.randint(1,2)
    if d == 2:
        d = -1
    return d


# This is the ramdom algorithm.
def randomize(cars, RANDOM_CARS):
    startboard = SaveBoard(cc.Board.board)
    score = 0
    while (cc.check() == False):
        r = random.randint(0, RANDOM_CARS)
        d = dirry()
        while(cars[r].move(d) == True):
            cars[r].move(d)
        score += 1
    print(cc.Board.board)
    print("You Won")
    print ("with " , score , " moves.")

    plt.imshow(cc.Board.board)
    plt.show()
    cc.Board.board = copy.copy(startboard)




def SaveBoard(board):
    startboard = copy.copy(cc.Board.board)
    return startboard


def random_two(cars, RANDOM_CARS):
    score_list = []
    startboard = np.copy(cc.Board.board)
    for i in range(10):
        score = 0
        while (cc.check() == False):
            r = random.randint(0, RANDOM_CARS)
            d = dirry()
            while(cars[r].move(d) == True):
                cars[r].move(d)
            score += 1
        #print(cc.Board.board)
        #print("You Won")
        #print ("with " , score , " moves.")
        cc.Board.board = copy.copy(startboard)
        score_list.append(score)
    print(score_list)
    print(min(score_list))

def DFS(cars, RANDOM_CARS, MAX_MOVE):
    count = MAX_MOVE - 1
    print(cc.Board.board)
    startboard = SaveBoard(cc.Board.board)
    if count > 0:
        for i in range (RANDOM_CARS):
            if cars[i].move(1) :
                while bool(cars[i].move(1)) == True:
                    cars[i].move(1)
            else:
                while bool(cars[i].move(-1)) == True:
                    cars[i].move(-1)
            print(cc.Board.board)
            time.sleep(0.3)
            DFS(cars, RANDOM_CARS, count)
            if count == 1:
                cc.Board.board = copy.copy(startboard)
    else:
        print("geen oplossing")


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
                print("winning moves:",move )
                cc.Board.board = copy.copy(startboard)
                break
            cc.Board.board = copy.copy(startboard)
