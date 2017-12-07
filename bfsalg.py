import itertools
import test_carclass as cc

def BFS(car, maxmoves):

    startboard = SaveBoard(cc.Board.board)
    totcars = list(range(0, cc.TOTAL_CARS))
    for i in range(maxmoves - 1):
        movespace = list(itertools.product(totcars, repeat = i + 1))
        print("amount of moves currently on:", i)
        for move in movespace:
            move = list(move)
            for auto in move:
                if car[auto].move(-1):
                    car[auto].move(-1)
                elif car[auto].move(1):
                    car[auto].move(1)
            if cc.check():
                print("you won in", i + 1, "moves")
                print("winning moves:",move )
                break
            cc.Board.board = copy.copy(startboard)
