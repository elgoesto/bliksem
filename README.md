# Lightning


## The game
In Rush Hour, a sliding block logic game, you have to battle the gridlock as you slide the blocking vehicles out of the way for the red car to exit. Cars can only move in the direction in which they are placed on the board. Cars cannot move outside of the board and cars cannot move on a spot where an other car is already parked.

<img src=https://github.com/elgoesto/bliksem/blob/master/speelbord.gif width="255">

## Getting Started
When you download this project you will get 3 different alogrithms to solve Rush Hour boards with different sizes and difficulties. The goal is to solve the game with as less moves as possible. 

First, the user have to implement the game to solve in classes/carclass Game().

<p>' pick a board between 1 - 7:  "games/game[...].csv" ' </p>
<p> game = pd.read_csv("games/testgame.csv", delimiter = "\t") </p>

Due to the user friendly interface it is pretty straigth forward to solve a board. The program will promt the user for wich algorithm you want to solve the selected board with.



### Installing
To run this program you will need to install the following software:
* Python 3
* Numpy
* Pandas
* Matplotlib
* Itertools


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
