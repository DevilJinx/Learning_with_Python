theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)

# Running result:
#  | |
# -+-+-
#  | |
# -+-+-
#  | |
# Turn for X. Move on which space?
# mid-L
#  | |
# -+-+-
# X| |
# -+-+-
#  | |
# Turn for O. Move on which space?
# mid-M
#  | |
# -+-+-
# X|O|
# -+-+-
#  | |
# Turn for X. Move on which space?
# low-M
#  | |
# -+-+-
# X|O|
# -+-+-
#  |X|
# Turn for O. Move on which space?
# low-L
#  | |
# -+-+-
# X|O|
# -+-+-
# O|X|
# Turn for X. Move on which space?
# top-L
# X| |
# -+-+-
# X|O|
# -+-+-
# O|X|
# Turn for O. Move on which space?
# top-R
# X| |O
# -+-+-
# X|O|
# -+-+-
# O|X|
# Turn for X. Move on which space?
# top-M
# X|X|O
# -+-+-
# X|O|
# -+-+-
# O|X|
# Turn for O. Move on which space?
# mid-R
# X|X|O
# -+-+-
# X|O|O
# -+-+-
# O|X|
# Turn for X. Move on which space?
# low-R
# X|X|O
# -+-+-
# X|O|O
# -+-+-
# O|X|X