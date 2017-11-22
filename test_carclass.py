import numpy as np
import csv
import pandas as pd
import random
import sys
import functies as fun


# Import the csv file of the game you want to play.
' pick a board between 1 - 7:  "games/game[...].csv" '
spel = pd.read_csv("games/game2.csv", delimiter = "\t")

# Define constants.
VERTICAL = 1
HORIZONTAL = 2
DOWN = 1
UP = -1
RIGHT = 1
LEFT = -1
EMPTY = 0
BSIZE = int(spel.iloc[0]["BSIZE"])
TOTAL_CARS = len(spel.index)
RANDOM_CARS = TOTAL_CARS - 1
WIN_X = BSIZE - 1
WIN_Y = int((WIN_X) / 2)

board = np.zeros((BSIZE, BSIZE))


class Car():
    "class to make cars"

    def __init__(self, car_id, y, x, orient, size):
        self.y = y
        self.x = x
        self.car_id = car_id
        self.orient = orient
        self.size = size
        if orient == VERTICAL:
            self.last = y + size
        elif orient == HORIZONTAL:
            self.last = x + size

        # Place every car on the board, based on its' orient.
        if orient == VERTICAL:
            board[y:size+y,x] = car_id
        elif orient == HORIZONTAL:
            board[y,x:size+x] = car_id



    # Function to move the cars by changing the values on the board.
    def move(self, direction):
        for i in range(BSIZE):
            for j in range(BSIZE):

                # If you find the location of the car, proceed.
                if board[i][j] == self.car_id:

                    # Check if the given move is valid, if so, move the car on the board.
                    if self.orient == VERTICAL:

                        if (direction == DOWN and (i + self.size) < BSIZE and \
                            board[i + self.size][j] == EMPTY) \
                            or \
                            (direction == UP and (i + direction) >= EMPTY and \
                            board[i + direction][j] == EMPTY):

                            if direction == DOWN:
                                i_coordinate = i
                            else:
                                i_coordinate = i + self.size - 1

                            base_i = i + direction
                            base_j = j_coordinate = j

                        else:
                            return False

                    else:
                        if (direction == RIGHT and (j + self.size) < BSIZE and \
                            board[i][j + self.size] == EMPTY) \
                            or \
                            (direction == LEFT and (j + direction) >= EMPTY and \
                            board[i][j + direction] == EMPTY):

                            if direction == RIGHT:
                                j_coordinate = j
                            else:
                                j_coordinate = j + self.size - 1

                            base_i = i_coordinate = i
                            base_j = j + direction

                        else:
                            return False

                    board[i_coordinate][j_coordinate] = EMPTY
                    Car(self.car_id, base_i, base_j, self.orient, self.size)
                    check()

# Function to check if car number 1 is on the winning coordinates.
def check():
    if board[WIN_Y][WIN_X] == 1:
        return True
    else:
        return False
