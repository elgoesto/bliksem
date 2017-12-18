import copy
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib import colors
from classes import carclass as cc



# Function for the visualisation of the state of the board.
def visualise(board, TOTAL_CARS, RANDOM_CARS):
    color_list= ["white", "red"]
    remaining_colors = ["yellow", "pink", "orange", "blue", "green", "black",
    "brown", "magenta", "purple", "violet", "beige", "cyan"]

    # For every car on the board, except for the red car, append a color
    # from remaining_colors to color_list.
    for i in range(RANDOM_CARS):
        color_list.append(remaining_colors[i % len(remaining_colors)])

    cmap = colors.ListedColormap(color_list)
    bounds = [0.0]
    NUMBER_OF_BOUNDS = TOTAL_CARS + 1

    # Set the bounds so that you can assign the colors to the white space and cars.
    for i in range(NUMBER_OF_BOUNDS):
        bound = i + 0.5
        bounds.append(bound)

    # Create a plot to show all of the cars, with their colors.
    fig, ax = plt.subplots()
    norm = colors.BoundaryNorm(bounds, cmap.N)
    ax.imshow(board, cmap=cmap, norm=norm)
    return plt.show()


# Function to make a copy of the startposition of the board.
def SaveBoard(board):
    startboard = copy.copy(cc.Board.board)
    return startboard


# Function to create a list of all of the possible moves within the current
# state of the board.
def possible_moves(cars, dontmove = -1):
    possible_moves = []
    for i in range(cc.Game.TOTAL_CARS):
        if cars[i].possible_move() == True and i != dontmove:
            possible_moves.append(i)
    return possible_moves
