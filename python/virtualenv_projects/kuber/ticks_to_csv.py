#!/Users/ansuman/Github/Projects/python/virtualenv/bin/python

"""
Subscribe to raw ticks data.
Add timestamp to the ticks data and update a csv file.
cmd = ""
cmd += "echo  \"" + DATA >> " + FileName
os.system(cmd)
"""

# import sys
# import time
import configparser
import zmq
import json
import time
import os

config = configparser.ConfigParser()
config.read('kuber.conf')

zmq_conf = config['ZMQ CONFIGURATION']
publish_port = zmq_conf['publish_port']
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt_string(zmq.SUBSCRIBE, '')
socket.bind("tcp://127.0.0.1:" + str(publish_port))


while True:
    tick = json.loads(socket.recv())

    # We get a list of instruments.
    # Now decode the list and prepare the format of csv file.
    #
    # 'Timestamp','instrument_token','ltp', 'ltq', 'avg', 'vol',
    # 'tot_buy', 'tot_sell', 'Open', 'High', 'Low', 'Close'
    # {'tradeable': True, 'mode': 'quote', 'instrument_token': 13873410,
    # 'last_price': 173.0, 'last_quantity': 40, 'average_price': 173.9,
    # 'volume': 2299600, 'buy_quantity': 0, 'sell_quantity': 0, 'ohlc': {'open':
    # 155.0, 'high': 200.0, 'low': 142.95, 'close': 154.85}, 'change':
    # 11.721020342266714, 'depth': {}}
    tsp = round(time.time() * 1000)

    for inst in tick:
        cmd = ''
        file_name = str(inst['instrument_token']) + '_ticks.csv'
        data = (tsp,
                inst['instrument_token'], inst['last_price'],
                inst['last_quantity'], inst['average_price'],
                inst['volume'], inst['buy_quantity'],
                inst['sell_quantity'],
                inst['ohlc']['open'],
                inst['ohlc']['high'],
                inst['ohlc']['low'],
                inst['ohlc']['close']
                )
        cmd += 'echo ' + str(data)[1:-1] + ' >> ' + file_name
        print(cmd)
        os.system(cmd)
