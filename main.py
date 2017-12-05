import test_carclass as cc
import functies as fun

# Initialize cars on the board.
cars = cc.Board.makecars(cc.Car, cc.TOTAL_CARS, cc.spel)

# Apply the random algorithm to solve the game
fun.randomize(cars, cc.RANDOM_CARS)
