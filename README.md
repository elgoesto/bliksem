# Lightning


## The game
In Rush Hour, a sliding block logic game, you have to battle the gridlock as you slide the blocking vehicles out of the way for the red car to exit. 

<img src=https://github.com/elgoesto/bliksem/blob/master/speelbord.gif width="255">

## Installing
To run this program you will need to install the following software:
* Python 3
* Numpy
* Pandas

## Instructions
* First you will need to choose with which set-up of the board you would like to play.
* Then a representation of the game is shown to the user.
  * Every 0 represents an empty space, at which the cars are able to drive to.
  * The 1 represents Lightning McQueen, the car to unpark.
  * Every other number represents all of the other cars parked on the board.
* (NOT YET) The user will be prompted which car needs to be moved and in which direction. Limitations: 
  * A car can only move in the direction at which it is pointing, horizontal or vertical. 
  * A car can only move on empty spaces, so it is not possible to park a car where another car is already parked. 
  * A car cannot move outside of the board. 
* To win the game you will need to move the red car, the car with number 1, completely to the right side of the board. 


## Authors
Lotte Nelson
David van der Velden
Justo van der Werf
