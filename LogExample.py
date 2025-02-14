import logging


logging.basicConfig(level = logging.INFO,
                    format="We have a message from %(levelname)s in %(asctime)s ")
# logging.basicConfig(filename='log1402.txt',
#                     filemode='w',
#                     level= logging.DEBUG)
logging.debug('Debug level')
logging.info('Info message')

logging.warning('This is warning')
logging.error('Сталася передбачувана помилка')
logging.critical('Critical Error')