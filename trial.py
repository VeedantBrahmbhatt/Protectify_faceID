# import logging
#
# # Configure the logging format
# logging.basicConfig(
#     level=logging.DEBUG,  # Set the desired log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S'
# )
#
# # Create a logger
# logger = logging.getLogger('my_logger')
#
# # Create a log file handler
# file_handler = logging.FileHandler('my_app.log')
#
# # Set the log file handler's log level (optional)
# file_handler.setLevel(logging.DEBUG)
#
# # Create a console handler
# console_handler = logging.StreamHandler()
#
# # Set the console handler's log level (optional)
# console_handler.setLevel(logging.INFO)
#
# # Create a formatter for the handlers (optional)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
# console_handler.setFormatter(formatter)
#
# # Add the handlers to the logger
# logger.addHandler(file_handler)
# logger.addHandler(console_handler)
#
# # Log some messages
# logger.debug('This is a debug message.')
# logger.info('This is an info message.')
# logger.warning('This is a warning message.')
# logger.error('This is an error message.')
# logger.critical('This is a critical message.')



########################################################################################################################
import schedule
import time

def job():
    print('Job Executed at ',time.strftime('%Y-%m-%d %H:%M:%S'))

if __name__=='__main__':
    schedule.every(3).seconds.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)




















