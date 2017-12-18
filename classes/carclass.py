import numpy as np
import csv
import pandas as pd



class Game():

    # Import the csv file of the game you want to play.
    ' pick a board between 1 - 7:  "games/game[...].csv" '
    game = pd.read_csv("games/testgame.csv", delimiter = "\t")

    # Define constants.
    BSIZE = int(game.iloc[0]["BSIZE"])
    TOTAL_CARS = len(game.index)
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
            Board.board[y:(size + y), x] = car_id
        elif orient == self.HORIZONTAL:
            Board.board[y, x:(size + x)] = car_id

    def resetcar(self):
        if self.orient == self.VERTICAL:
            Board.board[self.y:(self.size + self.y), self.x] = 0
        elif self.orient == self.HORIZONTAL:
            Board.board[self.y, self.x:(self.size + self.x)] = 0


    def possible_move(self):
        for i in range(Game.BSIZE):
            for j in range(Game.BSIZE):

                # If you find the location of the car, proceed.
                if Board.board[i][j] == self.car_id:

                    # Check if the car can move
                    if self.orient == self.VERTICAL:

                        if ((i + self.size) < Game.BSIZE and \
                            Board.board[i + self.size][j] == self.EMPTY) \
                            or \
                            ((i - 1) >= self.EMPTY and \
                            Board.board[i - 1][j] == self.EMPTY):

                            return True
                        return False
                    else:
                        if ((j + self.size) < Game.BSIZE and \
                            Board.board[i][j + self.size] == self.EMPTY) \
                            or \
                            ((j - 1) >= self.EMPTY and \
                            Board.board[i][j - 1] == self.EMPTY):

                            return True
                        return False

    # Function to move the cars by changing the values on the board.
    def move(self, direction):
        for i in range(Game.BSIZE):
            for j in range(Game.BSIZE):

                # If you find the location of the car, proceed.
                if Board.board[i][j] == self.car_id:

                    # Check if the given move is valid, if so, move the car on the board.
                    if self.orient == self.VERTICAL:

                        if (direction == self.DOWN and (i + self.size) < Game.BSIZE and \
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
                            self.x = base_j
                            self.y = base_i
                        else:
                            return False

                    else:
                        if (direction == self.RIGHT and (j + self.size) < Game.BSIZE and \
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
                            self.x = base_j
                            self.y = base_i
                        else:
                            return False

                    Board.board[i_coordinate][j_coordinate] = self.EMPTY
                    Car(self.car_id, base_i, base_j, self.orient, self.size)
                    return True

class Board():
    "Class to keep track of the board"

    board = np.zeros((Game.BSIZE, Game.BSIZE))
    # Function to create all the cars of the chosen ,'game', game and add them to cars.
    def makecars(Car, TOTAL_CARS, game):
        cars = []
        for car in range(TOTAL_CARS):
            cars.append(Car(int(game.iloc[car]['car_id']), int(game.iloc[car]['y']),
                            int(game.iloc[car]['x']), int(game.iloc[car]['orient']),
                            int(game.iloc[car]['size'])))
        return cars


class Lists():
    movelist = []
    boardlist = []

# Function to check if car number, with card_id 1 is on the winning coordinates.
def check():
    WIN_X = Game.BSIZE - 1
    WIN_Y = int((WIN_X) / 2)

    if Board.board[WIN_Y][WIN_X] == 1:
        return True
    else:
        return False
