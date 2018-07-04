# 空棋盘
# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 
#             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 
#             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
# 新棋盘
theBoard = {'top-L': 'O', 'top-M': 'X', 'top-R': 'O', 
            'mid-L': 'X', 'mid-M': 'O', 'mid-R': 'X', 
            'low-L': 'O', 'low-M': 'X', 'low-R': 'O'}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)

# Running result:
# 空棋盘：
#  | |
# -+-+-
#  | |
# -+-+-
#  | |
# 新棋盘：
# O|X|O
# -+-+-
# X|O|X
# -+-+-
# O|X|O
