import numpy as np
import csv

#constants
BSIZE = 6
VERTICAL = 1
HORIZONTAL = 2
DOWN = 1
RIGHT = 1
UP = -1
LEFT = -1

winningy = int((BSIZE - 1) / 2)
winningx = BSIZE - 1

board = np.zeros((BSIZE,BSIZE))


# make function to place cars on the board
# set coordinate and orintation
# orientation 1 = vertical, 2 = horizontal
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

        # Place car vertical
        if orient == VERTICAL:
            board[y:size+y,x] = car_id

        # Place car horizontal
        elif orient == HORIZONTAL:
            board[y,x:size+x] = car_id

        else:
            print("error")

    def check(self):
        print(board)
        print("******************************")
        if board[winningy][winningx] == 1:
            print("you won!")


    def move(self, direction):

        for i in range(BSIZE):
            for j in range(BSIZE):
                if board[i][j] == self.car_id:
                    if self.orient == VERTICAL:
                        if direction == 1 and board[i + self.size][j] == 0:
                            board[i][j] = 0
                            Car(self.car_id, i + direction, j, self.orient, self.size)
                            return self.check()
                        elif direction == -1 and board[i + direction][j] == 0:
                             board[i+self.size-1][j] = 0
                             Car(self.car_id, i + direction, j, self.orient, self.size)
                             return self.check()
                        else:
                            print("invalid move")
                            break
                    elif self.orient == HORIZONTAL:
                        if direction == 1 and board[i][j + self.size] == 0:
                            board[i][j] = 0
                            Car(self.car_id, i, j + direction, self.orient, self.size)
                            return self.check()
                        elif direction == -1 and board[i][j + direction] == 0:
                             board[i][j + self.size-1] = 0
                             Car(self.car_id, i, j + direction, self.orient, self.size)
                             return self.check()
                        else:
                            print("invalid move")
                            break


# examples how to place cars

car1 = Car(1, 2, 3, 2, 2)
car2 = Car(2, 0, 3, 2, 3)

print(board)
print("******************************")
car1.move(RIGHT)

# car1.move(UP)
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
