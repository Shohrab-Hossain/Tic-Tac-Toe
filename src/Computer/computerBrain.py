from Computer.computerLib import *

def computer_brain(game_data, computer_char, player_char):
    data = getData(game_data, player_char, computer_char)

    # checking Computer's last move to win, if any
    computer_move = checkWinningMove('computer', game_data, data)
    if(computer_move == 'none'):
        # checking Player's last move, to block Player's win
        computer_move = checkWinningMove('player', game_data, data)
        if(computer_move == 'none'):
            # initiating Triangle-Attack
            computer_move = triangleAttack(game_data, player_char, computer_char)
            if(computer_move == 'none'):
                # initaiting first move of the game
                computer_move = firstMethod(game_data, data, player_char, computer_char)
                if(computer_move == 'none'):
                    # finding any blank space to move
                    computer_move = findBlank(game_data)                    
            
    return computer_move if computer_move.isnumeric() else 'exit'   # this makes sure that the computed move for computer is a number and there is no error, if error caught 'exit' is used to leave the game 
            
