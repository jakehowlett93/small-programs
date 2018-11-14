'''
Two player Tic Tac Toe
'''
import random

def choose_symbol():
    '''
    takes input x or o
    returns list of choices ordered by input
    '''
    while True:
        symbol_choice = input('Player 1 choose a symbol! x or o:  ').lower()
        if symbol_choice == 'x':
            return ['x', 'o']
            
        elif symbol_choice == 'o':
            return ['o', 'x']
        else:
            print('Please choose either x or o')

def draw_board(board):
    '''
    takes indexes 1 - 9 of a list
    prints the values to the screen with the gameboard drawn around them
    '''
    print(f'{board[7]}|{board[8]}|{board[9]}')
    print(f'-|-|-')
    print(f'{board[4]}|{board[5]}|{board[6]}')
    print(f'-|-|-')
    print(f'{board[1]}|{board[2]}|{board[3]}')

def choose_position(board):
    '''
    prompts user to input a position
    loops until:
    - input is between 1 and 9
    - chosen position is empty
    '''
    position = 0
    
    while True:
        try:
            if board[position] != ' ':
                position = int(input('This position is already taken! Try another: '))
            elif position not in range(1, 10): 
                position = int(input('Choose a position to place your symbol (1-9): '))
            else:
                return position
        except:
            print('looks like you didnt enter an integer for position')

def random_player():
    turn = random.choice(['player1', 'player2'])
    return turn

def win_check(board, symbol):
    
    return ((board[7] == symbol and board[8] == symbol and board[9] == symbol) or # across the top
    (board[4] == symbol and board[5] == symbol and board[6] == symbol) or # across the middle
    (board[1] == symbol and board[2] == symbol and board[3] == symbol) or # across the bottom
    (board[7] == symbol and board[4] == symbol and board[1] == symbol) or # down the middle
    (board[8] == symbol and board[5] == symbol and board[2] == symbol) or # down the middle
    (board[9] == symbol and board[6] == symbol and board[3] == symbol) or # down the right side
    (board[7] == symbol and board[5] == symbol and board[3] == symbol) or # diagonal
    (board[9] == symbol and board[5] == symbol and board[1] == symbol)) # diagonal

def check_board_full(board):

    for position in range(1,10):
        if board[position] == ' ':
            return False
    return True

def play_again():
    play_again = ''
    while play_again != 'y' and play_again != 'n':
        play_again = input('Would you like to play again? (y/n): ')
    if play_again == 'y':
        return True
    else:
        return False


while True:
    #sets up the game
    board = [' '] * 10
    print('Welcome to tic tac toe')
    player_symbols = choose_symbol()
    player1_symbol = player_symbols[0]
    player2_symbol = player_symbols[1]
    turn = random_player()
    draw_board(board)
    game_on = True

    while game_on:
        if turn == 'player1':
            print("player1's turn!")
            position = choose_position(board)
            board[position] = player1_symbol
            if win_check(board, player1_symbol):
                print('Congratulations player1 wins!!')
                game_on = False
            elif check_board_full(board) == True:
                print('The game is a Draw')
                game_on = False
            else:
                turn = 'player2'
        else:
            print("player2's turn!")
            position = choose_position(board)
            board[position] = player2_symbol
            if win_check(board, player2_symbol) == True:
                print('Congratulations! Player2 wins!!')
                game_on = False
            elif check_board_full(board) == True:
                print('The game is a draw!!')
                game_on = False
            else:
                turn = 'player1'    
        
        draw_board(board)

    replay = play_again()
    if replay == False:
        break

