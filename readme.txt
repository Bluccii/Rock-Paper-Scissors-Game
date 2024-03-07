Author: Ivan Wu
Date: March 7th, 2024
Time spent on the project: ~20 minutes
Language(s) project was made in: Python

How I made this Project:

1. I imported the random library in order to create a 
    random chosen variable.

2. I initialized two variables, one denoting the choise of the user
    named "userChoice" and anotherone denoting the randomly generated
    choice of the "other" user named "randomChoice".

3. Then there are several conditional if-statements which run depending
    on whether or not the user or the computer (other user) has won.

    a. In the first 3 conditionals, we're checking to see if the computer
        won, and if so, output specific messages, the most important one 
        being that the user has lost.

    b. The 4th if-statement denotes a tie, when the user and the computer 
        chooses the same thing and prints output accordingly.

    c. The else-statement denotes any state in which the user has won, therefore
        output is to be printed that the user has won.


Extra: 

1. I added a while loop, like in my previous game, Number Guessing Game,
    in order to fix quality of life elements such as:
        - Allowing you to see the number of wins of both player 1 and player 2
        - Allowing you to play multiple games in one sitting
        - Allows user to enter the amount of rounds they'd like to play
        - Allows user to see overall stats of the game printed at the end of the game
        
2. Added a feature where the terminal gets cleared after every round for a 
    simpler reading experience on the user's side
        - Imported time and os
        - After every round, sleep the program for 5 seconds using time.sleep()
        - after the 5 seconds, clear the terminal using 
            - os.system('clear') - macOs/Linux
            - os.system('cls') - Windows
 