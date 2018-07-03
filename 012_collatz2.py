import sys
def collatz(number):
    print(number)
    if number == 1:
        sys.exit()
    elif number % 2 == 1:
        t = 3 * number + 1
        collatz(t)
    else:
        t=number // 2
        collatz(t)
     
     
def test():
    print('Enter number:')
    try:
        number  = int(input())
        collatz(number)
    except ValueError as verror:
            print('ValueError: You need to input an integer.')
         
test()