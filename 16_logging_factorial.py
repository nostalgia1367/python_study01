import logging

logging.basicConfig(level=logging.DEBUG, filename='log.txt',
                    format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of Program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n+1):
        if not i:
            continue
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')