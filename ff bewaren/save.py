
def trymoveset(cars, moveset):
    for car in moveset:
        if cars[car].move(1):
            while cars[car].move(1) == True:
                cars[car].move(1)
            print(cc.Board.board)
        else:
            while cars[car].move(-1) == True:
                cars[car].move(-1)
