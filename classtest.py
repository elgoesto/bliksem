import numpy as np
import cs50


#constants
BSIZE = 6

board = np.zeros((BSIZE,BSIZE))


# make cars, horizontal and verical, niet meer nodig
# car2h = np.array([1,1])
# car2v = np.array([[1],[1]])


# make function to place cars on the board
# set coordinate and orintation
# orientation 1 = vertical, 2 = horizontal
class Car():
    "class to make cars"

    def __init__(self, y, x, orient, size, car_id):

        # Place car vertical
        if orient == 1:
            board[y:size+y,x] = car_id

        # Place car horizontal
        elif orient == 2:
            board[y,x:size+x] = car_id

        else:
            print(error)







# examples how to place cars
car1 = Car(2, 3, 1, 2, 1)
car2 = Car(0, 3, 2, 3, 2)


print(board)


# Make function to move, where direction 1 = left/up and 2 = right/down
# Step direction: +1 or -1
# def move(car_id, stepdir):
    # kijken of er niet al een auto staat, of het board niet ophoudt
    # vertical geplaatste auto
    # if orient == 1:
        # board[]
