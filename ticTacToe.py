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


def checkIfWon(board, letter):
    # check top row
    if (board['top-L'] == board['top-M'] == board['top-R'] == letter):
        return True
    # check mid row
    elif (board['mid-L'] == board['mid-M'] == board['mid-R'] == letter):
        return True
    # check low row
    elif (board['low-L'] == board['low-M'] == board['low-R'] == letter):
        return True
    # check first col
    elif (board['top-L'] == board['mid-L'] == board['low-L'] == letter):
        return True
    # check second col
    elif (board['top-M'] == board['mid-M'] == board['low-M'] == letter):
        return True
    # check third col
    elif (board['top-R'] == board['mid-R'] == board['low-R'] == letter):
        return True
    # check first diagonal
    elif (board['top-L'] == board['mid-M'] == board['low-R'] == letter):
        return True
    # check second diagonal
    elif (board['top-R'] == board['mid-M'] == board['low-L'] == letter):
        return True
    else:
        return False


def main():
    turn = 'X'
    tempBoard = theBoard.copy()
    print('\nHere are the names of the locations on the board:\n')
    print('top-L|top-M|top-R')
    print('-----+-----+-----')
    print('mid-L|mid-M|mid-R')
    print('-----+-----+-----')
    print('low-L|low-M|low-R')
    print('\nCASE IS IMPORTANT!\n')
    for i in range(0, 9):
        printBoard(tempBoard)
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
        while move not in tempBoard.keys():
            print('Invalid space. Please enter it again.')
            move = input()
        while not isEmpty(tempBoard, move):
            print('That spot is taken, please try again.')
            move = input()
        tempBoard[move] = turn
        # check if won here
        if checkIfWon(tempBoard, turn):
            break
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    print('\n\n\n')
    print('Game over!', turn, 'won!!')
    printBoard(tempBoard)

    print('Play again? (y/n)')
    response = input()
    if response == 'y':
        print('\n\n\n')
        main()
    else:
        exit()


main()
