import test_carclass as cc
import pandas as pd
import numpy as np

class Board():

    def __init__(self, spel):
        self.BSIZE = int(spel.iloc[0]["BSIZE"])
        self.TOTAL_CARS = len(spel.index)
        self.RANDOM_CARS = self.TOTAL_CARS - 1
        self.WIN_X = self.BSIZE - 1
        self.WIN_Y = int((self.WIN_X) / 2)
        self.board = np.zeros((self.BSIZE,self.BSIZE))

    def makecars(self, Car, spel):
        cars = []

        for car in range(self.TOTAL_CARS):
            cars.append(Car(int(spel.iloc[car]['car_id']), int(spel.iloc[car]['y']),
                            int(spel.iloc[car]['x']), int(spel.iloc[car]['orient']),
                            int(spel.iloc[car]['size'])), self.board)
        return cars


    def randomize2(cars, RANDOM_CARS):
        startboard = SaveBoard(cc.board)
        score = 0
        scorelist = []
        for i in range (10):
            while (cc.check() == False):
                r = random.randint(0, RANDOM_CARS)
                d = dirry()
                while(cars[r].move(d) == True):
                    cars[r].move(d)
                score += 1
            print(cc.board)
            cc.board = copy.copy(startboard)
            #startboard = SaveBoard(cc.board)
            print("You Won")
            print ("with " , score , " moves.")
            scorelist.append(score)
            score = 0
        print(scorelist)


        def DFS(cars, RANDOM_CARS, MAX_MOVE):
            count = MAX_MOVE - 1
            if count != 0:
                for i in range (RANDOM_CARS):
                    if cars[i].move(1):
                        cars[i].move(1)
                        print(cc.board)
                        time.sleep(0.3)
                    else:
                        cars[i].move(-1)
                        print(cc.board)
                        time.sleep(0.3)
                    DFS(cars, RANDOM_CARS, count)
            else:
                print("geen oplossing")
                cc.board = startboard
                SaveBoard(cc.board)
