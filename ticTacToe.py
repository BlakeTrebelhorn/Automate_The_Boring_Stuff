theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def checkIfWon(board):
    # check top row
    if board['top-L'] == board['top-M'] == board['top-R']:
        return True
    # check mid row
    elif board['mid-L'] == board['mid-M'] == board['mid-R']:
        return True
    # check low row
    elif board['low-L'] == board['low-M'] == board['low-R']:
        return True
