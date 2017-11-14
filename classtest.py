import numpy as np
import csv
import pandas as pd

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
spel = pd.read_csv("games/game1.csv", delimiter = "\t")

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
        print(board, "\n")
        if board[winningy][winningx] == 1:
            print("you won!")

    # Function to move the cars by chaning the values on the board.
    def move(self, direction):
        for i in range(BSIZE):
            for j in range(BSIZE):
                if board[i][j] == self.car_id:

                    # Change values on board based on the orient and direction.
                    if self.orient == VERTICAL:
                        if direction == DOWN and board[i + self.size][j] == EMPTY_SPACE:
                            # Change x coordinate of the car with the direction.
                            board[i][j] = EMPTY_SPACE
                            Car(self.car_id, i + direction, j, self.orient, self.size)
                            return self.check()
                        elif direction == UP and board[i + direction][j] == EMPTY_SPACE:
                            board[i+self.size-1][j] = EMPTY_SPACE
                            Car(self.car_id, i + direction, j, self.orient, self.size)
                            return self.check()
                        else:
                            print("invalid move", "\n")
                            return self.check()

                    elif self.orient == HORIZONTAL:
                        if direction == RIGHT and board[i][j + self.size] == EMPTY_SPACE:
                            board[i][j] = EMPTY_SPACE
                            Car(self.car_id, i, j + direction, self.orient, self.size)
                            return self.check()
                        elif direction == LEFT and board[i][j + direction] == EMPTY_SPACE:
                            board[i][j + self.size-1] = EMPTY_SPACE
                            Car(self.car_id, i, j + direction, self.orient, self.size)
                            return self.check()
                        else:
                            print("invalid move", "\n")
                            return self.check()


# examples how to place cars
cars = []

for auto in range(len(spel.index)):

    cars.append(Car(int(spel.iloc[auto]['car_id']),int(spel.iloc[auto]['y']), int(spel.iloc[auto]['x']),
                        int(spel.iloc[auto]['orient']),int(spel.iloc[auto]['size'])))

print(board)
print("******************************")
print(cars)
cars[1].move(DOWN)
cars[7].move(UP)
cars[2].move(DOWN)
cars[6].move(LEFT)

# print(board)
# print()
# car2.move(LEFT)
# print(board)
#




# Make function to move, where direction 1 = left/up and 2 = right/down
# Step direction: +1 or -1
# def move(car_id, stepdir):
    # kijken of er niet al een auto staat, of het board niet ophoudt
    # vertical geplaatste auto
    # if orient == 1:
        # board[]
