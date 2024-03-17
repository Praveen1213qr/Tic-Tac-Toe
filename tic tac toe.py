# Tic Tac Toe game in Python

# Function to draw the Tic Tac Toe board
def draw_board(board):
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('---------')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('---------')
    print(f'{board[6]} | {board[7]} | {board[8]}')

# Function to check if a player has won
def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full
def check_full(board):
    return ' ' not in board

# Function to switch player turns
def switch_player(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'

# Main game loop
def main():
    board = [' '] * 9
    player = 'X'

    while True:
        draw_board(board)
        print(f'Player {player}\'s turn')
        move = int(input('Enter your move (1-9): ')) - 1

        if board[move] == ' ':
            board[move] = player
            if check_win(board, player):
                print(f'Player {player} wins!')
                break
            elif check_full(board):
                print('The board is full. It\'s a draw!')
                break
            else:
                player = switch_player(player)
        else:
            print('That space is already occupied. Try again.')

if __name__ == '__main__':
    main()