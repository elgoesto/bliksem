import carclass as cc
import functies as fun
# import board

def main():
    # Initialize cars on the board.
    cars = cc.Board.makecars(cc.Car, cc.TOTAL_CARS, cc.spel)

    

    print ("test board met random")
    fun.randomize(cars, cc.RANDOM_CARS, cc.TOTAL_CARS)

if __name__ == "__main__":
    main()
