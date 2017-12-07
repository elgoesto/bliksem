import carclass as cc
import functies as fun
import test_randomtwo as rt

def main():
    # Initialize cars on the board.
    cars = cc.Board.makecars(cc.Car, cc.TOTAL_CARS, cc.spel)

    # Apply the random algorithm to solve the game
    fun.randomize(cars, cc.RANDOM_CARS)

if __name__ == "__main__":
    main()
