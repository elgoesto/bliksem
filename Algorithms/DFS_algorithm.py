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

movelist = []
boardlist = []

def DFST(cars, MAX_MOVE, dontmove = -1):
    count = MAX_MOVE - 1

    if count > 0:
        moves = fun.possible_moves(cars, dontmove)
        for car in moves:
            car_number = car + 1

            if cars[car].move(1):
                base = 1
                place_back = -1
            elif cars[car].move(-1):
                base = -1
                place_back = 1

            while cars[car].move(base) == True:
                cars[car].move(base)
            movelist.append(car_number)
            print(movelist)
            boardlist.append(copy.copy(cc.Board.board))

            if cc.check() == True:
                print(cc.Board.board)
                print(movelist)
                for board in boardlist:
                    print(board)
                    print("")
                    print(movelist)
                sys.exit("you won")

            while bool(cars[car].move(place_back)) == True:
                cars[car].move(place_back)
            movelist.pop()
            boardlist.pop()

            DFS(cars, count, car)


def DFS(cars, MAX_MOVE, dontmove = -1):
    count = MAX_MOVE - 1
    if count > 0:
        moves = fun.possible_moves(cars, dontmove)
        for car in moves:
            if cars[car].move(1):
                while bool(cars[car].move(1)) == True:
                    cars[car].move(1)
                movelist.append(car + 1)
                print(movelist)
                boardlist.append(copy.copy(cc.Board.board))
                #time.sleep(0.1)
                if cc.check() == True:
                    print(cc.Board.board)
                    print(movelist)
                    for board in boardlist:
                        print(board)
                        print("")
                        print(movelist)
                    sys.exit("you won")
                DFS(cars, count, car)
                while bool(cars[car].move(-1)) == True:
                    cars[car].move(-1)
            else:
                while bool(cars[car].move(-1)) == True:
                    cars[car].move(-1)
                #time.sleep(0.1)
                movelist.append(car + 1)
                print(movelist)
                boardlist.append(copy.copy(cc.Board.board))
                if cc.check() == True:
                    print(cc.Board.board)
                    print(movelist)
                    for board in boardlist:
                        print(board)
                        print("")
                        print(movelist)
                    sys.exit("you won")
                DFS(cars, count, car)
                while bool(cars[car].move(1)) == True:
                    cars[car].move(1)
            movelist.pop()
            boardlist.pop()
