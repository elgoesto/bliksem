import test_carclass as cc
import random
import copy
import numpy as np
import time



# part of the ramdom algorithm, this picks a ramdom direction.
def dirry():
    d = random.randint(1,2)
    if d == 2:
        d = -1
    return d


# This is the ramdom algorithm.
def randomize(cars, RANDOM_CARS):
    score = 0
    while (cc.check() == False):
        r = random.randint(0, RANDOM_CARS)
        d = dirry()
        while(cars[r].move(d) == True):
            cars[r].move(d)
        print(cc.Board.board)
        time.sleep(0.5)
        score += 1
    print(cc.Board.board)
    print("You Won")
    print ("with " , score , " moves.")
    return score

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
