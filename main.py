from classes import carclass as cc
from functions import functions as fun
from algorithms import random_algorithm as rand
from algorithms import BFS_algorithm as bfs
from algorithms import DFS_algorithm as dfs
from numba import jit
# import board

@jit
def main():
    # Create constants.
    RANDOM = 1
    BFS = 2
    DFS = 3
    DFS_Lotte = 4

    # Initialize cars on the board.
    cars = cc.Board.makecars(cc.Car, cc.Game.TOTAL_CARS, cc.Game.game)

    print("Choose 1 to run the random algorithm.")
    print("Choose 2 to run the Breadth First Search algorithm.")
    print("Choose 3 to run the Depth First Search algorithm.")
    print("Choose 4 Lotte DFS")

    # Prompt the user for input.
    var = input("Please enter something: ")

    # Check the user input and implement the choosen algorithm.
    if var.isalpha():
        print("Error, you did not enter one of these options.")

    elif int(var) == RANDOM:
        print ("Start random algorithm.")
        rand.randomize(cars, cc.Game.RANDOM_CARS, cc.Game.TOTAL_CARS)

    elif int(var) == BFS:
        print("Start Breadth First Search algorithm.")
        bfs.BFS(cars, 16)

    elif int(var) == DFS:
        print("Start Depth First Search algorithm.")
        print(cc.Board.board)
        dfs.DFS(cars, 15)

    elif int(var) == DFS_Lotte:
        print("Start test Lotte")
        dfs.DFST(cars, 17)

    else:
        print("Error, you did not enter one of these options.")


if __name__ == "__main__":
    main()
