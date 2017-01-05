theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def isEmpty(board, space):
    if board[space] == ' ':
        return True
    else:
        return False


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def checkIfWon(board):
    # check top row
    if board['top-L'] == board['top-M'] == board['top-R'] & board['top-L'] != ' ':
        return True
    # check mid row
    elif board['mid-L'] == board['mid-M'] == board['mid-R'] & board['mid-L'] != ' ':
        return True
    # check low row
    elif board['low-L'] == board['low-M'] == board['low-R'] & board['low-L'] != ' ':
        return True
    # check first col
    elif board['top-L'] == board['mid-L'] == board['low-L'] & board['top-L'] != ' ':
        return True
    # check second col
    elif board['top-M'] == board['mid-M'] == board['low-M'] & board['top-M'] != ' ':
        return True
    # check third col
    elif board['top-R'] == board['mid-R'] == board['low-R'] & board['top-R'] != ' ':
        return True
    # check first diagonal
    elif board['top-L'] == board['mid-M'] == board['low-R'] & board['top-L'] != ' ':
        return True
    # check second diagonal
    elif board['top-R'] == board['mid-M'] == board['low-L'] & board['top-R'] != ' ':
        return True
    else:
        return False


turn = 'X'
for i in range(0, 9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    while move not in theBoard.keys():
        print('Invalid space. Please enter it again.')
        move = input()
    while not isEmpty(theBoard, move):
        print('That spot is taken, please try again.')
        move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
