import test_carclass as cc
import random



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
    print(cc.Board.board)
    print("You Won")
    print ("with " , score , " moves.")
    return score


def random_two(cars, RANDOM_CARS):
    score_list = []
    for i in range(100):
        score = 0
        while (cc.check() == False):
            r = random.randint(0, RANDOM_CARS)
            d = dirry()
            while(cars[r].move(d) == True):
                cars[r].move(d)
            score += 1
        print(cc.Board.board)
        print("You Won")
        print ("with " , score , " moves.")
        score_list.append(score)
    return score_list
