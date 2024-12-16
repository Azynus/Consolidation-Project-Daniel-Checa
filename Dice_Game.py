# Tuple Out Dice Game
# The goal is to score the most points or be the first to reach the target score.
# Players take turns rolling three dice per turn.
# If all three dice show the same number, the player is tuple'd out and scores 0 points for that turn.
# If two dice show the same number, they become fixed and cannot be re-rolled.
# Unfixed dice can be re-rolled until the player tuple's out or chooses to stop.
# The player's score for the turn is the sum of the three dice when they decide to stop.
# The game ends when a player reaches the target score.

import random

def roll_dice():
    """Rolls three dice and returns their values as a tuple.
    Each die generates a random integer between 1 and 6."""
    return random.randint(1,6), random.randint(1,6), random.randint(1,6)

def is_tuple_out(dice):
    """Checks if all three dice have the same value (tuple out).
    If all dice show the same number, the player scores 0 for their turn."""
    return (dice[0] == dice[1] == dice[2])
#The function get_fixed_dice is fine for checking which dice are fixed based on pairs, but it doesn't handle all cases. 
def get_fixed_dice(dice):
    """Determines which dice are fixed based on matching pairs.
    Fixed dice are dice that cannot be rolled again."""
    if dice[0] == dice[1] == dice[2]:  # All dice match (tuple out)
        return [True, True, True]  # All dice are fixed
    elif dice[0] == dice[1] and dice[0] != dice[2]:
        return [True, True, False]  # The first two dice are fixed
    elif dice[1] == dice[2] and dice[1] != dice[0]:
        return [False, True, True]  # The last two dice are fixed
    elif dice[0] == dice[2] and dice[0] != dice[1]:
        return [True, False, True]  # The first and third dice are fixed
    return [False, False, False]  # No dice are fixed if no pairs match


def player_turn(player, turn, target_score):
    """Handles a single players turn and returns their score
    Allows to player to roll dice, decide whether to reroll, and accumulate points"""
    print(f"\nPlayer {turn + 1}'s turn:")
    
    #Initiliaze a dice dictionary 
    dice_status = {
        'dice': roll_dice(), #Roll three dice
        'fixed': [False, False, False] #No dice are fixed
    }

    print(f'Initial roll: {dice_status["dice"]}') 

    if is_tuple_out(dice_status['dice']): #Check to see if player tupled out
        print('Tuple Out! You have scored 0 points this round.')
        return 0 

    dice_status['fixed'] = get_fixed_dice(dice_status['dice']) #Determine which dice are fixed

    while True: # Allow the player to reroll unfixed dice until they choose to stop or tuple out
        print(f"Fixed dice: {['Yes' if fixed else 'No' for fixed in dice_status['fixed']]}")  # Display which dice are fixed
        choice = input("Do you want to re-roll? (yes/no): ").strip().lower()  # Ask if the player wants to reroll

        if choice not in ['yes', 'no']: #validates the player's input
            print("Invalid input. please enter 'yes' or 'no'. ")
            continue

        if choice == 'no':
        # If the player chooses to stop, calculate the score for this turn
            score = sum(dice_status['dice'])  # The score is the sum of all three dice
            print(f"You stopped with a score of {score} points.")
            return score

        #Reroll any unfixed dice and keep any fixed ones
        dice_status['dice'] = [
            dice_status['dice'][i] if dice_status['fixed'][i] else random.randint(1, 6) 
            for i in range(3)
            ]
       
        print(f'New Roll: {dice_status["dice"]}') #Updated roll

        if is_tuple_out(dice_status['dice']):
            print('Tuple Out! You have scored 0 points this round.')
            return 0
    
        dice_status['fixed'] = get_fixed_dice(dice_status['dice']) #Recalculate fixed dice after reroll

def play_game(target_score = 50):
    """Plays the game until the player reaches the target score.
    Manages the game loop, tracks scores, and determines the winner"""
    try:
        players = int(input('Enter the number of players: ')) #Get the number of players
        if players <= 0:
            print('Number of players must be atleat 1')
            return
    except ValueError:
        print('Invalid input. Please enter a valid number.')
        return

    scores = [0] * players #Create a list of scores for each player
    turn = 0 #Start with player 1

    while True:
    #Check if any player reached the target score
        for score in scores:
            if score >= target_score:
                print(f'\nPlayer {scores.index(max(scores)) + 1} wins with {max(scores)} points') #Announces the winner
                return
        #Handle the current player's turn    
        scores[turn] += player_turn(turn, turn, target_score) #Add player's turn score to total
        print(f'Player {turn + 1} total score: {scores[turn]}') #Display player's total score
    
        #Moves to the next player
        turn = (turn + 1) % players

#Start the game
play_game()
