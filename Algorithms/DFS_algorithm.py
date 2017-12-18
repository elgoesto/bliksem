import copy
from classes import carclass as cc
from functions import functions as fun
import sys





def DFS(cars, MAX_MOVE, dontmove = -1):

    count = MAX_MOVE - 1
    if count > 0:
        moves = fun.possible_moves(cars, dontmove)
        for car in moves:
            initial_x = cars[car].x
            initial_y = cars[car].y
            car_number = car + 1
            if cars[car].move(-1):
                base = -1
            else:
                base = 1

            while cars[car].move(base) == True:
                cars[car].move(base)
            cc.Lists.movelist.append(car_number)
            print(cc.Lists.movelist)
            cc.Lists.boardlist.append(copy.copy(cc.Board.board))
            if cc.check() == True:
                print(cc.Board.board)
                print("")
                print(cc.Lists.movelist)
                sys.exit("You won!")

            DFS(cars, count, car)
            cars[car].resetcar()
            cars[car] = cc.Car(car_number, initial_y, initial_x, cars[car].orient, cars[car].size)
            cc.Lists.movelist.pop()
