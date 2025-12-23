tic_tac_toe_board = [['x ','x',' x',]]
print(f'___{tic_tac_toe_board[0][0]}|___{tic_tac_toe_board[0][1]}|___{tic_tac_toe_board[0],[2]}')
print(f'___{tic_tac_toe_board[0][0]}|___{tic_tac_toe_board[0][1]}|___{tic_tac_toe_board[0],[2]}')
print(f'___{tic_tac_toe_board[0][0]}|___{tic_tac_toe_board[0][1]}|___{tic_tac_toe_board[0],[2]}')



# The game board is represented by a dictionary
theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

def printBoard(board):
    """
    Prints the current state of the tic-tac-toe board.
    The keys in the dictionary are arranged to match a 3x3 grid,
    like a keyboard's number pad.
    """
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def checkWin(board, player):
    """
    Checks if the current player has won the game by covering all 3
    spaces in any row, column, or diagonal.
    """
    # Check horizontal wins
    if board['7'] == board['8'] == board['9'] == player:
        return True
    if board['4'] == board['5'] == board['6'] == player:
        return True
    if board['1'] == board['2'] == board['3'] == player:
        return True
    # Check vertical wins
    if board['7'] == board['4'] == board['1'] == player:
        return True
    if board['8'] == board['5'] == board['2'] == player:
        return True
    if board['9'] == board['6'] == board['3'] == player:
        return True
    # Check diagonal wins
    if board['7'] == board['5'] == board['3'] == player:
        return True
    if board['9'] == board['5'] == board['1'] == player:
        return True
    return False

def game():
    """
    The main game loop that handles turns, input, and game status checks.
    """
    turn = 'X'
    count = 0
    while count < 9:
        printBoard(theBoard)
        print("It's your turn, " + turn + ". Move to which place?")
        move = input()
        
        if move in theBoard and theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled or invalid input. Try again!")
            continue

        if count >= 5: # A win is only possible after at least 5 moves
            if checkWin(theBoard, turn):
                printBoard(theBoard)
                print("\nGame Over.")
                print("**** " + turn + " won! ****")
                return

        # Switch turns
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    # If the loop finishes without a winner, it's a tie
    printBoard(theBoard)
    print("\nGame Over.")
    print("It's a Tie!!")

if __name__ == "__main__":
    game()