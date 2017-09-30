#!/Users/ansuman/Github/Projects/python/virtualenv/bin/python
#
"""
Create a historical database of NSE stocks.
"""

import logging


def logging_init(logFile):
    """ Initialize the logger
    :param logFile: Log file.
    :return: logger or None
    """
    try:
        logger = logging.getLogger('nse_db')
        hdlr = logging.FileHandler(logFile)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        hdlr.setFormatter(formatter)
        logger.addHandler(hdlr)
        logger.setLevel(logging.INFO)
        return logger
    except Exception as e:
        print(e)

    return None


def main():
    """
    1) Get a list of all scrips from Nifty.
    2) Get EOD historical data from the year 2000 for each scrip.
    3) Create a table for each scrip.
    4) Create a table containing <scrip name>, <last updated date>
    5) Update the database daily
    """
    logger = logging_init('./logger_ex.log')
    logger.info('Logging some stuff..')

    x = 1
    log_msg = 'logging some more stuff.. ' + str(x)
    logger.info(log_msg)

    logger.info('Another logging example %s',str(2))

if __name__ == '__main__':
    main()
