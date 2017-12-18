import copy
from classes import carclass as cc
from functions import functions as fun
import sys

# Function for the implementation of a Depth First Search.
def DFS(cars, MAX_MOVE, dontmove = -1):
    count = MAX_MOVE - 1

    if count > 0:
        # Check which cars can move on the current state of the board.
        moves = fun.possible_moves(cars, dontmove)

        # Try every move in moves.
        for car in moves:
            initial_x = cars[car].x
            initial_y = cars[car].y
            car_number = car + 1
            if cars[car].move(-1):
                base = -1
            else:
                base = 1

            # Move the car as far as possible.
            while cars[car].move(base) == True:
                cars[car].move(base)

            cc.Lists.movelist.append(car_number)
            print(cc.Lists.movelist)
            cc.Lists.boardlist.append(copy.copy(cc.Board.board))

            # Check if the board is in the winning state.
            if cc.check() == True:
                print(cc.Board.board)
                print("")
                print(cc.Lists.movelist)
                sys.exit("You won!")

            # Recursion, try the next move.
            DFS(cars, count, car)
            cars[car].resetcar()
            cars[car] = cc.Car(car_number, initial_y, initial_x, cars[car].orient, cars[car].size)
            cc.Lists.movelist.pop()
