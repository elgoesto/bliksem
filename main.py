import carclass as cc
import functies as fun
import board

def main():
    # Initialize cars on the board.
    cars = cc.Board.makecars(cc.Car, cc.TOTAL_CARS, cc.spel)

    # Apply the BFS algorithm to solve the game
    print("test board met bfs")
    fun.BFS(cars, 5)

    # apply the random algorithm
    print ("test board met random")
    fun.randomize(cars, cc.RANDOM_CARS)

if __name__ == "__main__":
    main()
