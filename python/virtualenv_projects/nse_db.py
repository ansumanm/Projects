#!/Users/ansuman/Github/Projects/python/virtualenv/bin/python
#
"""
Create a historical database of NSE stocks.
"""

import logging
import sqlite3
from sqlite3 import Error
import ssl
from nsetools import Nse
import time
# import datetime
# import pdb
# from pprint import pprint

# To get over the following error:
# <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate
# verify failed (_ssl.c:748)>
ssl._create_default_https_context = ssl._create_unverified_context


class scrip:
    """A scrip entry in the scripsTable"""
    def __init__(self, scripCode=None, scripDesc=None, fromDate=None,
                 lastUpdatedDate=None, currentMarketPrice=None,
                 entryTimeStamp=None):
        self.scripCode = scripCode
        self.scripDesc = scripDesc
        self.fromDate = fromDate
        self.lastUpdatedDate = lastUpdatedDate
        self.currentMarketPrice = currentMarketPrice
        self.entryTimeStamp = entryTimeStamp
        pass

    @classmethod
    def init_scrip_with_values(cls, scripCode, scripDesc, fromDate,
                               lastUpdatedDate, currentMarketPrice,
                               entryTimeStamp):
        return cls(scripCode, scripDesc, fromDate, lastUpdatedDate,
                   currentMarketPrice, entryTimeStamp)

    @classmethod
    def init_scrip_from_tuple(cls, tupleObj):
        return cls(*tupleObj)

    def get_tuple(self):
        return (self.scripCode, self.scripDesc, self.fromDate,
                self.lastUpdatedDate, self.currentMarketPrice,
                self.entryTimeStamp)

    def __repr__(self):
        return 'scrip({}, {}, {}, {}, {}, {})'.format(self.scripCode,
                                                      self.scripDesc,
                                                      self.fromDate,
                                                      self.lastUpdatedDate,
                                                      self.currentMarketPrice,
                                                      self.entryTimeStamp)

    def __str__(self):
        return 'scrip({}, {}, {}, {}, {}, {})'.format(self.scripCode,
                                                      self.scripDesc,
                                                      self.fromDate,
                                                      self.lastUpdatedDate,
                                                      self.currentMarketPrice,
                                                      self.entryTimeStamp)


def create_connection(db_file):
    """ create a connection to the sqlite database specified
    by db_file.
    :param db_file: database file
    :return: Connection object or None.
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def create_table(conn, create_table_sql):
    """ Create a table from the create_table_sql statement.
    :param conn: Connection Object.
    :param create_table_sql: A create table statement.
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

    return None


def scripsTable_insert_scrip(conn, scrip):
    """
    TODO Create a scrip object that can be inserted into this table.
    """
    sql_stmt = """
                INSERT INTO scripsTable(scripCode,scripDesc,
                fromDate,lastUpdatedDate,currentMarketPrice,
                entryTimeStamp) VALUES(?,?,?,?,?,?)
                """

    try:
        cur = conn.cursor()
        cur.execute(sql_stmt, scrip.get_tuple())
    except Exception as e:
        print(e)


def scripsTable_query_scrip_by_code(conn, scripCode):
    """ Query scripsTable for the scripCode. """
    sql_qry_stmt = "SELECT * FROM scripsTable WHERE scripCode=?"
    cur = conn.cursor()
    cur.execute(sql_qry_stmt, (scripCode,))
    tupleObj = cur.fetchone()
    cur.close()

    if tupleObj is None:
        return None

    return scrip.init_scrip_from_tuple(tupleObj)


def get_all_nse_scrips():
    """ Get scrip list from nseindia.com
    """
    try:
        nse = Nse()
        all_stock_codes = nse.get_stock_codes()
        return all_stock_codes
    except Exception as e:
        print(e)

    return None


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
    # pdb.set_trace()
    database = 'nse_data.db'

    # We will maintain historical data from 2000-01-01
    never = '1999-12-31'

    sql_create_scrips_table = """ CREATE TABLE IF NOT EXISTS scripsTable (
                                        scripCode TEXT PRIMARY KEY,
                                        scripDesc TEXT,
                                        fromDate TEXT,
                                        lastUpdatedDate TEXT,
                                        currentMarketPrice REAL,
                                        entryTimeStamp REAL
                                        ); """

    # Start logging.
    logger = logging_init('/tmp/nse_db.log')

    if logger is None:
        print('Failed to create logger.')
        return None

    logger.info('Creating a connection with %s.', database)
    # Create a database connection.
    conn = create_connection(database)

    if conn is not None:
        logger.info('Connection with %s successful.', database)
        create_table(conn, sql_create_scrips_table)
        cur = conn.cursor()
    else:
        print("Error: Couldn't create database connection.")
        logger.error('Connection with %s failed.', database)
        return None

    all_scrip_codes = get_all_nse_scrips()

    if all_scrip_codes is not None:
        for scripCode, scripDesc in all_scrip_codes.items():
            scripObj = scripsTable_query_scrip_by_code(conn, scripCode)
            if scripObj is not None:
                print(scripObj)
            else:
                logger.info('%s not found in scripsTable', scripCode)
                # Insert the scripCode to the database.
                print('Adding scrip Code: {} Desc: {}'.format(scripCode,
                                                              scripDesc))
                scripObj = scrip.init_scrip_with_values(scripCode,
                                                        scripDesc,
                                                        never,
                                                        never,
                                                        0,
                                                        time.time())
                scripsTable_insert_scrip(conn, scripObj)
                logger.info('Inserted %s to scripsTable', scripDesc)

    else:
        print("Error: Couldn't get scrip codes.")
        logger.error("Couldn't get scrip codes.")
        # Query to the site nseindia.com failed.
        # Lets use the scrip list from our database for further
        # operations.

    # Close the SQL database connection.
    cur.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
