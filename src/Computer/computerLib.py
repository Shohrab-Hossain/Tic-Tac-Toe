import random   # this default module is used for random selection

def getData(game_data, player_char, computer_char):   # this function generates data about the board
    data = {
        'player_row1' : 0,   # this stores how many player-characters are in row1
        'player_row2' : 0,
        'player_row3' : 0,
        'player_col1' : 0,   # this stores how many player-characters are in col1
        'player_col2' : 0,
        'player_col3' : 0,
        'player_dia1' : 0,   # this stores how many player-characters are in diagonal1
        'player_dia2' : 0,
        'computer_row1' : 0,   # this stores how many computer-characters are in row1
        'computer_row2' : 0,
        'computer_row3' : 0,
        'computer_col1' : 0,   # this stores how many computer-characters are in col1
        'computer_col2' : 0,
        'computer_col3' : 0,
        'computer_dia1' : 0,   # this stores how many computer-characters are in diagonal1
        'computer_dia2' : 0,
        'blank_row1' : 0,   # this stores how many blank-spaces are in row1
        'blank_row2' : 0,
        'blank_row3' : 0,
        'blank_col1' : 0,
        'blank_col2' : 0,
        'blank_col3' : 0,
        'blank_dia1' : 0,
        'blank_dia2' : 0,
        'total_blank': 0,   # this stores how many blank-spaces are in all-over-the-board
    }

    def index_helper(index):   # this function generates corresponding row/colo/diagonal number for each point of the board
        if index == 1:
            return ['row1', 'col1', 'dia1']
        elif index == 2:
            return ['row1', 'col2']
        elif index == 3:
            return ['row1', 'col3', 'dia2']
        elif index == 4:
            return ['row2', 'col1']
        elif index == 5:
            return ['row2', 'col2', 'dia1', 'dia2']
        elif index == 6:
            return ['row2', 'col3']
        elif index == 7:
            return ['row3', 'col1', 'dia2']
        elif index == 8:
            return ['row3', 'col2']
        elif index == 9:
            return ['row3', 'col3', 'dia1']


    # checking each item in board
    for x in range(1,10):
        value = 'b' + str(x)
        positions = index_helper(x)

        if(game_data[value]==player_char):
            for position in positions:
                data['player_'+position] += 1

        elif(game_data[value]==computer_char):
            for position in positions:
                data['computer_'+position] += 1

        else:
            for position in positions:
                data['blank_'+position] += 1
            data['total_blank'] += 1


    # returning the computed data
    return data


def checkWinningMove(name, game_data, data):   # this function finds move that will be a winning move for 'name'
    def reverse_index_helper(x):
        if(x=='_row1'):
            return ['1', '2', '3']
        elif(x=='_row2'):
            return ['4', '5', '6']
        elif(x=='_row3'):
            return ['7', '8', '9']
        elif(x=='_col1'):
            return ['1', '4', '7']
        elif(x=='_col2'):
            return ['2', '5', '8']
        elif(x=='_col3'):
            return ['3', '6', '9']
        elif(x=='_dia1'):
            return ['1', '5', '9']
        elif(x=='_dia2'):
            return ['3', '5', '7']


    default_move = 'none'
    directions = ['_row1', '_row2', '_row3', '_col1', '_col2', '_col3', '_dia1', '_dia2']
    
    for direction in directions:
        if(data[name+direction]==2 and data['blank'+direction]==1):
            default_move = list( filter(lambda x: game_data['b'+x]==' ', reverse_index_helper(direction)) )   # this filter out the position that is blank (' ')
            default_move = default_move[0]   # list is not required, only the position is needed. So taking the first element of the list
            break
        else:
            continue

    return str(default_move)   # this 'default_move' must be String


def triangleAttack(game_data, player_char, computer_char):
    default_move = 'none'

    # inorder to initiate Trinagle-Attack the middle point 'b5' must be computer-character
    if(game_data['b5']==computer_char):
        if(game_data['b1']==game_data['b5']):
            attack_point = ['2', '4']
        elif(game_data['b3']==game_data['b5']):
            attack_point = ['2', '6']
        elif(game_data['b7']==game_data['b5']):
            attack_point = ['4', '8']
        elif(game_data['b9']==game_data['b5']):
            attack_point = ['6', '8']
        else:
            return default_move

        for x in attack_point:
            if game_data['b'+x] != player_char:   # this checks that the attack-point is not occupied by Player-charater
                if x=='2':
                    positions = ['1', '3', '8']
                elif x=='4':
                    positions = ['1', '7', '6']
                elif x=='6':
                    positions = ['3', '9', '4']
                elif x=='8':
                    positions = ['7', '9', '2']
                
                checked_position = list( filter(lambda x: game_data['b'+x]!=player_char, positions) )
                if len(positions) == len(checked_position):
                    default_move = x
                    break
        
    return default_move

def firstMethod(game_data, data, player_char, computer_char):
    default_move = 'none'

    if data['total_blank'] == 9:   # this is for first move
        return random.choice(['1', '3', '7', '9'])
    else:
        if data['total_blank'] == 7:   # this is for second move
            for x in range(1,10):
                if game_data['b'+str(x)] == player_char:
                    player_position = str(x)
                if game_data['b'+str(x)] == computer_char:
                    computer_position = str(x)
            
            diagonal1 = ['1', '5', '9']
            diagonal2 = ['3', '5', '7']

            if diagonal1.count(player_position)!=0 or diagonal2.count(player_position)!=0:
                if diagonal1.count(player_position)==diagonal2.count(computer_position) or diagonal2.count(player_position)==diagonal1.count(computer_position):
                    if computer_position == '1':
                        return '9'
                    elif computer_position == '9':
                        return '1'
                    elif computer_position == '3':
                        return '7'
                    else:
                        return '3'
            return '5'
        else:
            return default_move

def findBlank(game_data):   # this function finds blank space to move
    default_move = list( filter(lambda x: game_data['b' + str(x)]==' ', range(1,10)) )   # this filter out the positions that are blank (' ')
    default_move = random.choice(default_move)   # this selects a random postion from the available blank positions. 'random' module is imported above the code
    
    return str(default_move)   # this 'default_move' must be String
