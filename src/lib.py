def game_type_selection():
    print('\n' +
          '--------------------------------\n' +
          'How do you want to play:\n'  +
          '\t[1] with another PLAYER\n' +
          '\t[2] with COMPUTER\n')
    
    while(True):
        command = input('select an option (1/2): ')

        if(command == '1'):
            str = 'PvP'
            break
        elif(command == '2'):
            str = 'PvC'
            break
        else:
            print('Error: Please select a valid option.')
            continue
    
    print('\n--------------------------------\n\n')
    return str
            


def character_selection(game_type):
    if(game_type == 'PvP'):   # taking character for Player-vs-Player game 
         # taking Character for Player01
        player1_char = input("Choose a character for player 01 : ")
        player1_char = player1_char[0:1]    # making the character length 1

        # taking Character for Player02
        player2_char = input("Choose a character for player 02 : ")
        player2_char = player2_char[0:1]    # making the character length 1
        
        # this while loop checks that player02's character is different from player01
        while(True):
            if(player1_char == player2_char):
                print('\nError: Player 2 character must be different from player 1\n')
                player2_char = input("Chose a different character for player 02 : ")
                player2_char = player2_char[0:1]    # making the character length 1
            else:
                print(log_massage['game_started'])
                break

        return [player1_char, player2_char]
    
    elif(game_type == 'PvC'):   # taking character for Player-vs-Computer game
         # taking Character for Player01
        player_char = input("Choose a character for player : ")
        player_char = player_char[0:1]    # making the character length 1

        # generating character for computer, based on player01 character
        if(player_char.lower() == 'x'):
            computer_char = 'o'
        else:
            computer_char = 'x'

        return [computer_char, player_char]
    
    else:
        return ['error']


def print_board(game_data):
        placeholder1 = '       |       |       '
        placeholder2 = '-----------------------'
        
        print('\n\n\n\t\t{}'.format(placeholder1))
        print('\t\t   {}   |   {}   |   {}   '.format( game_data['b7'], game_data['b8'], game_data['b9'] ))
        print('\t\t{}\n\t\t{}\n\t\t{}'.format( placeholder1, placeholder2, placeholder1 ))
        print('\t\t   {}   |   {}   |   {}   '.format( game_data['b4'], game_data['b5'], game_data['b6'] ))
        print('\t\t{}\n\t\t{}\n\t\t{}'.format( placeholder1, placeholder2, placeholder1 ))
        print('\t\t   {}   |   {}   |   {}  '.format( game_data['b1'], game_data['b2'], game_data['b3'] ))
        print('\t\t{}\n\n\n'.format( placeholder1 ))


def get_winner(game_data, player1_char, player2_char):
        # checking Rows
        if game_data['b1'] == game_data['b2'] == game_data['b3']:
            winner=game_data['b1']
        elif game_data['b4'] == game_data['b5'] == game_data['b6']:
            winner=game_data['b4']
        elif game_data['b7'] == game_data['b8'] == game_data['b9']:
            winner=game_data['b7']
        
        # checking Columns
        elif game_data['b1'] == game_data['b4'] == game_data['b7']:
            winner=game_data['b1']
        elif game_data['b2'] == game_data['b5'] == game_data['b8']:
            winner=game_data['b2']
        elif game_data['b3'] == game_data['b6'] == game_data['b9']:
            winner=game_data['b3']
        
        # checking Diagonals
        elif game_data['b1'] == game_data['b5'] == game_data['b9']:
            winner=game_data['b1']
        elif game_data['b3'] == game_data['b5'] == game_data['b7']:
            winner=game_data['b3']

        else:
            winner='none'
        
        # returning the winner name
        if winner == player1_char:
            return 'player 01'
        elif winner == player2_char:
            return 'player 02'
        else:
            return 'none'    


log_massage = {
        'game_started': '\n' +
                        '------------------------------ \n' +
                        '|        Game Started.        |\n' +
                        '------------------------------ \n' ,
        
        'game_ended':   '\n' +
                        '---------------------------------- \n' +
                        '|    The game has been ended.    | \n' +
                        '---------------------------------  \n' ,

        'you_lose'  :   '\n' +
                        '--------------------------------------------\n' + 
                        '|             Sorry! You lose.             |\n' + 
                        '--------------------------------------------'   ,

        'you_win'   :   '\n' +
                        '-------------------------------------------\n'  + 
                        '|        Congratulations! You win.        |\n'  +
                        '-------------------------------------------'    ,

        'got_draw'  :  '\n' +
                        '-----------------------------------------\n' +
                        '|    AHH! No one wins. It is a draw.    |\n' +
                        '-----------------------------------------'
    }    