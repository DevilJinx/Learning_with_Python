import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')

# Running result:
# Type exit to exit.
# s
# You typed s.
# Type exit to exit.
# we
# You typed we.
# Type exit to exit.
# exit