# Lightning


## The game
In Rush Hour, a sliding block logic game, you have to battle the gridlock as you slide the blocking vehicles out of the way for the red car to exit. Cars can only move in the direction in which they are placed on the board. Cars cannot move outside of the board and cars cannot move on a spot where an other car is already parked.

<img src=https://github.com/elgoesto/bliksem/blob/master/speelbord.gif width="255">

## Getting Started
When you download this project you will get 3 different alogrithms to solve Rush Hour boards with different sizes and difficulties. The goal is to solve the game with as less moves as possible. 

main.py is the main program to run the different algorithms. In this file you will need to choose which algortihm you would like to run. You can do this by changing the following line of code on line 10:

* If you want to run the random algorithm:
  * fun.randomize(cars, cc.RANDOM_CARS)
* If you want to run the optimized random alogrithm:
  * fun.random_two(cars, cc.RANDOM_CARS)
* If you want to run the Depth First Search algorithm:
  * fun.BFS(cars, maxmoves)
  * You would probably want to run this algortihm on the games/testgame.csv board, cause this will take less time than the other boards.

carclass.py consists of two classes. One for the implementation of the cars and one for the implementation of the board. In this file you can choose which game you would like to play. You can do this by changing the game number, for example in stead of game2 in game3, in the following line of code:

* spel = pd.read_csv("games/game2.csv", delimiter = "\t")

functies.py consists of functions we have written to implement the algorithms.


### Installing
To run this program you will need to install the following software:
* Python 3
* Numpy
* Pandas
* Matplotlib

To install the software you can use pip install. For example, type the following commands in your terminal to install matplotlib:

1. python -mpip install -U pip
2. python -mpip install -U matplotlib

## Instructions, to run the program
* First you will need to choose which game you would like to play. In the getting started section is explained how you could do this.
* Once you have choosen the game you will need to choose which algorithm you would like to run. You can read the explanation on how to do this in the getting started section.
* After you have done all of this you can run the main.py file. Make sure you do this while running python3 in your terminal.  

## Other files
* In the map Games are several csv files. Every csv files contains the data to implement the startingposition of all the cars.
* In the file board.py some of our tests are written, you can ignore this file for now.
* Gitignore file

## Authors
Lotte Nelson,
David van der Velden en
Justo van der Werf
