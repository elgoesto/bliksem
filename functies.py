import carclass as cc
import random


def makecars(Car, TOTAL_CARS, spel):
    cars = []

    # Add every car in the game to the list cars.
    for car in range(TOTAL_CARS):
        cars.append(Car(int(spel.iloc[car]['car_id']), int(spel.iloc[car]['y']),
                        int(spel.iloc[car]['x']), int(spel.iloc[car]['orient']),
                        int(spel.iloc[car]['size'])))
    return cars



# part of the ramdom algorithm, this picks a ramdom direction.
def dirry():
    d = random.randint(1,2)
    if d == 2:
        d = -1
    return d


# This is the ramdom algorithm.
def randomize(cars, RANDOM_CARS):
    score = 0
    while (cc.check() == False):
        r = random.randint(0, RANDOM_CARS)
        d = dirry()
        while(cars[r].move(d) == True):
            cars[r].move(d)
        score += 1
    print(cc.board)
    print("You Won")
    print ("with " , score , " moves.")
    return score
