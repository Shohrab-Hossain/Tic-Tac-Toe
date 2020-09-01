from lib import *
from Computer.computerBrain import *


def start_play():
    
    # this dictionary holds the data of each movement
    game_data = {'b1':' ', 'b2':' ', 'b3':' ', 'b4':' ', 'b5':' ', 'b6':' ', 'b7':' ', 'b8':' ', 'b9':' '}
    
    # selecting game type
    game_type = game_type_selection()
    
    # taking Character for Players
    player_char = character_selection(game_type)
    
    # this for loop runs for 9steps and takes player movement one by one.
    for x in range(1,10):
        # printing player characters before each step
        str = ['Player 01', 'Player 02'] if game_type=='PvP' else ['Computer', 'Player']
        print(f'{str[0]} character is : {player_char[0]}')
        print(f'{str[1]} character is : {player_char[1]}')
        
        # this if-else statement checks wether the step is for Player 01 or Player 02/Computer
        if x%2 == 0 :
            selected_button = input(str[1] + " 's turn : ")
            character = player_char[1]
        else:
            if(game_type == 'PvP'):   # this will take input from Player 02
                selected_button = input(str[0] + "'s turn : ")
            else:   # this will take input from Computer
                selected_button = computer_brain(game_data, player_char[0], player_char[1])
                print(f"{str[0]}'s turn : {selected_button}")
            character = player_char[0]

        # if user choose to leave then exits
        if selected_button.lower() == 'exit':
            print(log_massage['game_ended'])
            break
        
        # this while loop validate the user input
        while(True):
            if selected_button.isnumeric() and int(selected_button) in range(1,10):
                if game_data['b'+selected_button] == ' ':
                    game_data['b'+selected_button] = character
                    break
                else:
                    selected_button = input('Error! Button is already taken. Select a new button : ')
            else:
                selected_button = input('Error! Select a button between 01 to 09 : ')
        
        print_board(game_data)

        # checking for winner
        if x > 4:
            winner = get_winner(game_data, player_char[0], player_char[1])
            if not winner == 'none':
                if(game_type == 'PvP'):
                    #print(f'-------------------------------------------\n|  Congratulations! {winner} is winner.  |\n-------------------------------------------')
                    break
                else:
                    if winner == 'player 01':   # Computer wins
                        print(log_massage['you_lose'])
                        break
                    else:   # Player wins
                        print(log_massage['you_win'])
                        break
    
        # game reached in last step, meaning no one wins 
        if x == 9:
            print(log_massage['got_draw'])

if __name__ == "__main__":
    start_play()
    while(True):
        command = input("\nPlay again [Y/N] : ")
        if command.lower()=='y':
            start_play()
        else:
            print('\nThank You.\n\n')
            break
    
    