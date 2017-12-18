import copy
import itertools
from classes import carclass as cc
import sys
from functions import functions as fun

# Function for the implementation of a Breath First Search.
def BFS(car, maxmoves):

    startboard = fun.SaveBoard(cc.Board.board)

    # Make list of all the cars on the board.
    totcars = list(range(0, cc.Game.TOTAL_CARS))
    for i in range(maxmoves ):
        print("amount of moves currently on:", i)

        # Get each possible set of moves, but don't save more then 1 movelist.
        for move in itertools.product(totcars, repeat = i + 1):
            move = list(move)

            # Execute the move list.
            for auto in move:
                if car[auto].move(-1):
                    while car[auto].move(-1) == True:
                        car[auto].move(-1)
                elif car[auto].move(1):
                    while car[auto].move(1) == True:
                        car[auto].move(1)
            if cc.check():
                print("you won in", i + 1, "moves")
                print("winning moves:", move)
                sys.exit()

            # Reset the board, for the next movelist.
            cc.Board.board = copy.copy(startboard)
