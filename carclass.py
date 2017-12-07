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
BSIZE = int(spel.iloc[0]["BSIZE"])
TOTAL_CARS = len(spel.index)
RANDOM_CARS = TOTAL_CARS - 1

class Car():
    "class to make cars"

    # Define Constants.
    VERTICAL = 1
    HORIZONTAL = 2
    DOWN = 1
    UP = -1
    RIGHT = 1
    LEFT = -1
    EMPTY = 0

    def __init__(self, car_id, y, x, orient, size):
        self.y = y
        self.x = x
        self.car_id = car_id
        self.orient = orient
        self.size = size
        if orient == self.VERTICAL:
            self.last = y + size
        elif orient == self.HORIZONTAL:
            self.last = x + size

        # Place every car on the board, based on its' orient.
        if orient == self.VERTICAL:
            Board.board[y:size+y,x] = car_id
        elif orient == self.HORIZONTAL:
            Board.board[y,x:size+x] = car_id

    # Function to move the cars by changing the values on the board.
    def move(self, direction):
        for i in range(BSIZE):
            for j in range(BSIZE):

                # If you find the location of the car, proceed.
                if Board.board[i][j] == self.car_id:

                    # Check if the given move is valid, if so, move the car on the board.
                    if self.orient == self.VERTICAL:

                        if (direction == self.DOWN and (i + self.size) < BSIZE and \
                            Board.board[i + self.size][j] == self.EMPTY) \
                            or \
                            (direction == self.UP and (i + direction) >= self.EMPTY and \
                            Board.board[i + direction][j] == self.EMPTY):

                            if direction == self.DOWN:
                                i_coordinate = i
                            else:
                                i_coordinate = i + self.size - 1

                            base_i = i + direction
                            base_j = j_coordinate = j
                        else:
                            return False

                    else:
                        if (direction == self.RIGHT and (j + self.size) < BSIZE and \
                            Board.board[i][j + self.size] == self.EMPTY) \
                            or \
                            (direction == self.LEFT and (j + direction) >= self.EMPTY and \
                            Board.board[i][j + direction] == self.EMPTY):

                            if direction == self.RIGHT:
                                j_coordinate = j
                            else:
                                j_coordinate = j + self.size - 1

                            base_i = i_coordinate = i
                            base_j = j + direction
                        else:
                            return False

                    Board.board[i_coordinate][j_coordinate] = self.EMPTY
                    Car(self.car_id, base_i, base_j, self.orient, self.size)
                    return True

class Board():
    "Class to keep track of the board"
    board = np.zeros((BSIZE, BSIZE))
    def makecars(Car, TOTAL_CARS, spel):
        cars = []

        # Add every car in the game to the list cars.
        for car in range(TOTAL_CARS):
            cars.append(Car(int(spel.iloc[car]['car_id']), int(spel.iloc[car]['y']),
                            int(spel.iloc[car]['x']), int(spel.iloc[car]['orient']),
                            int(spel.iloc[car]['size'])))
        return cars

# Function to check if car number 1 is on the winning coordinates.
def check():
    WIN_X = BSIZE - 1
    WIN_Y = int((WIN_X) / 2)

    if Board.board[WIN_Y][WIN_X] == 1:
        return True
    else:
        return False
