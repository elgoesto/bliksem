import carclass as cc
import functies as fun
import random_algorithm as rand
import BFS_algorithm as bfs
import DFS_algorithm as dfs
# import board

def main():
    # Initialize cars on the board.
    cars = cc.Board.makecars(cc.Car, cc.TOTAL_CARS, cc.spel)

    print("Choose 1 to run the random algorithm.")
    print("Choose 2 to run the Bredth First Search algorithm.")
    print("Choose 3 to run the Depth First Search algorithm.")

    var = input("Please enter something: ")
    print(var)

    # print("test board met BFS")
    # bfs.BFS(cars, 5)
    #
    # print("")
    if int(var) == 1:
        print ("Test board with random algorithm.")
        rand.randomize(cars, cc.RANDOM_CARS, cc.TOTAL_CARS)
    elif int(var) == 2:
        print("Test board with Breadth First Search.")
        bfs.BFS(cars, 5)
    elif int(var) == 3:
        print("Test board with Depth First Search.")
        dfs.DFS(cars, 5)
    else:
        print("Error, you did not enter one of these options.")

    # print("")
    #
    # print("test board met DFS")
    # dfs.DFS(cars, 5)

if __name__ == "__main__":
    main()
