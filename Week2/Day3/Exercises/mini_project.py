board = {
    '7': ' ', '8': ' ', '9': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '1': ' ', '2': ' ', '3': ' ',
}

def display_board(board):
    print('Welcome to TIC TAC TOE!')
    print('')
    print("TIC TAC TOE")
    print('***************')
    print('*  ' + board['7'] + ' | ' + board['8'] + ' | ' + board['9'] + '  *')
    print('* ---|---|--- *')
    print('*  ' + board['4'] + ' | ' + board['5'] + ' | ' + board['6'] + '  *')
    print('* ---|---|--- *')
    print('*  ' + board['1'] + ' | ' + board['2'] + ' | ' + board['3'] + '  *')
    print('***************')

def check_win(board, player):
    if (board['7'] == board['8'] == board['9'] == player or
        board['4'] == board['5'] == board['6'] == player or
        board['1'] == board['2'] == board['3'] == player or
        board['7'] == board['4'] == board['1'] == player or
        board['8'] == board['5'] == board['2'] == player or
        board['9'] == board['6'] == board['3'] == player or
        board['7'] == board['5'] == board['3'] == player or
        board['9'] == board['5'] == board['1'] == player):
        return True
    return False   

def game():
    grid = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}
    current_player = 'X'
    count = 0
    max_moves = 9

    while count < max_moves:
        display_board(grid)
        move = input(f"Hello, you are {current_player}. Please choose a spot on the board (1-9):\n> ")


        if move in grid and grid[move] == ' ':
            grid[move] = current_player
            count += 1
        elif move not in grid:
            print("Please choose a number between 1 and 9.")
            continue   
        else:
            print("Sorry, that place is already taken. Please choose another spot.")
            continue

        if count >= 5 and check_win(grid, current_player):
            display_board(grid)
            print(f"Player {current_player} has won!")
            return

        if count == max_moves:
            display_board(grid)
            print("Tie game!")
            return
        
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    game()