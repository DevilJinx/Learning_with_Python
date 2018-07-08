import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%) % (n)')
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')

# Running result:
#  2018-07-08 16:28:32,698 - DEBUG - Start of program
#  2018-07-08 16:28:32,698 - DEBUG - Start of factorial(%s%%) % (n)
#  2018-07-08 16:28:32,699 - DEBUG - i is 0, total is 0
#  2018-07-08 16:28:32,699 - DEBUG - i is 1, total is 0
#  2018-07-08 16:28:32,699 - DEBUG - i is 2, total is 0
#  2018-07-08 16:28:32,699 - DEBUG - i is 3, total is 0
#  2018-07-08 16:28:32,699 - DEBUG - i is 4, total is 0
#  2018-07-08 16:28:32,699 - DEBUG - i is 5, total is 0
#  2018-07-08 16:28:32,699 - DEBUG - End of factorial(5%)
# 0
#  2018-07-08 16:28:32,699 - DEBUG - End of program