# README

## Tuple Out Dice Game
Hello! Welcome to my dice game. A fun little game for 1 or more players. This program lets players take turns rolling dice, fixing pairs, and make strategic choices on whether to stop rolling or keep rolling and see if they can reach the target score.

## How it works:

### Objective:
Score the most points or be the first player to reach the target score of 50 points.

### Gameplay:
- Each player takes turns rolling a dice.
- If all three dice shown are the same number the player will tuple out and score 0 points for that turn.
- if the player rolls and two dice are the same number those dice will be fixed and cannot be rerolled.
- Players can continue rerolling any unfixed dice until they want to stop or they tuple out
- When a player choses to stop their roll will be sum of the three dice.
- The game will end as soon as one player reaches the target score of 50 points.

## How to Play
If you want to run it line by line have the file open in VS Code make sure you're in the right file path and press `shift+enter` if you have REPL Smart Send disabled you will have to highligh each block of code.

If you just want to run the script and not run it line by line open up your terminal in VS Code or in Miniconda make sure that you're on the right file path so if the python file is in your downloads and in VS Code you're in your documents file path move it over or go to wherever the file is. Enter this prompt in the terminal `python dice_game.py`
doing this will run the entire program without needing to run it line by line.

 ### Enter the number of players
 The program will prompt you to enter a certain number of players (Minimum of 1).

After that each player roll three dice, decide whether or not to keep rerolling any unfixed dice, avoid being tuple'd out, and aim to reach the 50 point target score.

## Program features 

### Dynamic Gameplay
Supports 1 or more players, making it perfect for solo play or group fun.

### User input validation
Ensures all user inputs like number of players or deciding whether to keep rolling are valid.

### Strategy Decisions
Encourages startegic conditions based on dice rolls and fixed pairs

### Randomness
Each dice roll is random adding an element of luck to the game.