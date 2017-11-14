import numpy as np
import csv
import pandas as pd
import random
import sys

# Define constants.
BSIZE = 6
VERTICAL = 1
HORIZONTAL = 2
DOWN = 1
RIGHT = 1
UP = -1
LEFT = -1
EMPTY_SPACE = 0

# If car 1 is on the winning coordinates, the game is finshed.
winningx = BSIZE - 1
winningy = int((winningx) / 2)

# Make two dimensional grit of zeros with the size BSIZE.
board = np.zeros((BSIZE,BSIZE))

# Import the csv file of the game you want to play.
spel = pd.read_csv("games/game2.csv", delimiter = "\t")

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

        # Place every car according to orient, if not possible print error.
        if orient == VERTICAL:
            board[y:size+y,x] = car_id
        elif orient == HORIZONTAL:
            board[y,x:size+x] = car_id
        else:
            print("error")

    # Function to check if car number 1 is on the winning coordinates.
    def check(self):
        if board[winningy][winningx] == 1:
            print("you won!")
            sys.exit("WON")
        return print(board, "\n")

    # Function to move the cars by chaning the values on the board.
    def move(self, direction):
        for i in range(BSIZE):
            for j in range(BSIZE):
                if board[i][j] == self.car_id:
                    # Change values on board based on the orient and direction.
                    if self.orient == VERTICAL:
                        if direction == 1 and (i + self.size) < BSIZE and board[i + self.size][j] == 0:
                            # Change x coordinate of the car with the direction.
                            board[i][j] = 0
                            Car(self.car_id, i + direction, j, self.orient, self.size)
                            self.check()
                        elif direction == -1 and (i + direction) >= 0 and board[i + direction][j] == 0:
                            board[i+self.size-1][j] = 0
                            Car(self.car_id, i + direction, j, self.orient, self.size)
                            self.check()
                        else:
                            print("invalid move", "\n")
                            return False
                    else:
                        if direction == 1 and (j + self.size) < BSIZE and board[i][j + self.size] == 0:
                            board[i][j] = 0
                            Car(self.car_id, i, j + direction, self.orient, self.size)
                            self.check()
                        elif direction == -1 and (j + direction) >= 0 and board[i][j + direction] == 0:
                            board[i][j + self.size-1] = 0
                            Car(self.car_id, i, j + direction, self.orient, self.size)
                            self.check()
                        else:
                            print("invalid move", "\n")
                            return False



# examples how to place cars
cars = []

for auto in range(len(spel.index)):

    cars.append(Car(int(spel.iloc[auto]['car_id']),int(spel.iloc[auto]['y']), int(spel.iloc[auto]['x']),
                        int(spel.iloc[auto]['orient']),int(spel.iloc[auto]['size'])))

print(board)
# cars[4].move(UP)
# cars[1].move(LEFT)
# cars[8].move(RIGHT)
# cars[6].move(UP)
# cars[6].move(UP)
# cars[6].move(UP)
# cars[6].move(UP)
# cars[6].move(UP)
# cars[8].move(RIGHT)
# print(board)
# print()
# car2.move(LEFT)
# print(board)
#

def dirry():
    d = random.randint(1,2)
    if d == 2:
        d = -1
    return d

for i in range(1000):
    r = random.randint(0,8)
    d = dirry()
    while(cars[r].move(d) == True):
        cars[r].move(d)



# Make function to move, where direction 1 = left/up and 2 = right/down
# Step direction: +1 or -1
# def move(car_id, stepdir):
    # kijken of er niet al een auto staat, of het board niet ophoudt
    # vertical geplaatste auto
    # if orient == 1:
        # board[]





# Make function to move, where direction 1 = left/up and 2 = right/down
# Step direction: +1 or -1
# def move(car_id, stepdir):
    # kijken of er niet al een auto staat, of het board niet ophoudt
    # vertical geplaatste auto
    # if orient == 1:
        # board[]
