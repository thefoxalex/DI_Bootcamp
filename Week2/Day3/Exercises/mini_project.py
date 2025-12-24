board = {
    '7': ' ', '8': ' ', '9': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '1': ' ', '2': ' ', '3': ' ',
}



def display_board(board):
    print('***************')
    print('*  ' + board['7'] + ' | ' + board['8'] + ' | ' + board['9'] + '  *')
    print('* ---|---|--- *')
    print('*  ' + board['4'] + ' | ' + board['5'] + ' | ' + board['6'] + '  *')
    print('* ---|---|--- *')
    print('*  ' + board['1'] + ' | ' + board['2'] + ' | ' + board['3'] + '  *')
    print('***************')
display_board(board)

def player_input(player):
    user1_position = input("Please enter a position on the board using the numbers 1-9 (e.g., for the upper right square, you would type in 9, like the layout of a number pad): ")
