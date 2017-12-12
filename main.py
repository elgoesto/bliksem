import carclass as cc
import functies as fun
import random_algorithm as rand
import BFS_algorithm as bfs
import DFS_algorithm as dfs
# import board

def main():
    # Initialize cars on the board.
    cars = cc.Board.makecars(cc.Car, cc.TOTAL_CARS, cc.spel)

    # print("test board met BFS")
    # bfs.BFS(cars, 5)
    #
    # print("")

    print ("test board met random")
    rand.randomize(cars, cc.RANDOM_CARS, cc.TOTAL_CARS)
    #
    # print("")
    #
    # print("test board met DFS")
    # dfs.DFS(cars, 5)

if __name__ == "__main__":
    main()
