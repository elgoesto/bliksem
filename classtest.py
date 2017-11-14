import numpy as np
import csv
import pandas as pd
import random
import sys

# Import the csv file of the game you want to play.
spel = pd.read_csv("games/game7.csv", delimiter = "\t")

# Define constants.
VERTICAL = 1
HORIZONTAL = 2
DOWN = 1
UP = -1
RIGHT = 1
LEFT = -1
EMPTY = 0
BSIZE = int(spel.iloc[0]["BSIZE"])
RANDOM_CARS = len(spel.index) - 1
WIN_X = BSIZE - 1
WIN_Y = int((WIN_X) / 2)

# Define variables.
cars = []

# Make two dimensional grit of zeros with the size BSIZE.
board = np.zeros((BSIZE,BSIZE))

# Initialize the board.
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

    # Function to check if car number 1 is on the winning coordinates.
    def check(self):
        if board[WIN_Y][WIN_X] == 1:
            print(board)
            print(score)
            sys.exit("YOU WON!")

    # Function to move the cars by changing the values on the board.
    def move(self, direction):
        for i in range(BSIZE):
            for j in range(BSIZE):

                # If you find the location of the car, proceed.
                if board[i][j] == self.car_id:

                    # Check if the given move is valid, if so, move the car on the board.
                    if self.orient == VERTICAL:
                        if direction == DOWN and (i + self.size) < BSIZE and \
                        board[i + self.size][j] == EMPTY:
                            board[i][j] = EMPTY
                            Car(self.car_id, i + direction, j,
                            self.orient, self.size)
                            self.check()

                        elif direction == UP and (i + direction) >= EMPTY and \
                        board[i + direction][j] == EMPTY:
                            board[i+self.size-1][j] = EMPTY
                            Car(self.car_id, i + direction, j,
                            self.orient, self.size)
                            self.check()

                        else:
                            return False
                    else:
                        if direction == RIGHT and (j + self.size) < BSIZE and \
                        board[i][j + self.size] == EMPTY:
                            board[i][j] = EMPTY
                            Car(self.car_id, i, j + direction,
                            self.orient, self.size)
                            self.check()

                        elif direction == LEFT and (j + direction) >= EMPTY and \
                        board[i][j + direction] == EMPTY:
                            board[i][j + self.size-1] = EMPTY
                            Car(self.car_id, i, j + direction,
                            self.orient, self.size)
                            self.check()
                        else:
                            return False


# Add every car in the game to the list cars.
for car in range(len(spel.index)):
    cars.append(Car(int(spel.iloc[car]['car_id']), int(spel.iloc[car]['y']),
                    int(spel.iloc[car]['x']), int(spel.iloc[car]['orient']),
                    int(spel.iloc[car]['size'])))

def dirry():
    d = random.randint(1,2)
    if d == 2:
        d = -1
    return d

score = 0
for i in range(1000000):
    r = random.randint(0, RANDOM_CARS)
    d = dirry()
    while(cars[r].move(d) == True):
        cars[r].move(d)
    score += 1
