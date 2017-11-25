#!/Users/ansuman/Github/Projects/python/virtualenv/bin/python

"""
The websocket publisher App. It receives ticks from zerodha for
the subscribed instruments and publishes them over the port.
"""
from kiteconnect import KiteConnect
from kiteconnect import WebSocket
import sys
# import time
import configparser
import ssl
import zmq
import json

ssl._create_default_https_context = ssl._create_unverified_context

config = configparser.ConfigParser()
config.read('kuber.conf')

login_conf = config['Login Configuration']
api_key = login_conf['api_key']
api_secret = login_conf['api_secret']
request_token = login_conf['request_token']

access_token = config['ACCESS INFO']

"""
Publisher Setup.
"""
zmq_conf = config['ZMQ CONFIGURATION']
publish_port = zmq_conf['publish_port']
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://127.0.0.1:" + str(publish_port))

"""
Websocket Configuration
"""
ws_conf = config['WS CONFIGURATION']
instruments = ws_conf['instruments'].split(',')
instruments = list(map(int, instruments))

"""
ce = {'instrument_token': '13873410', 'exchange_token': '54193',
      'tradingsymbol': 'BANKNIFTY17NOV25800CE', 'name': '', 'last_price':
      154.85, 'expiry': '2017-11-30', 'strike': 25800.0, 'tick_size': 0.05,
      'lot_size': 40, 'instrument_type': 'CE', 'segment': 'NFO-OPT', 'exchange':
      'NFO'}

pe = {'instrument_token': '13873666', 'exchange_token': '54194',
      'tradingsymbol': 'BANKNIFTY17NOV25800PE', 'name': '', 'last_price':
      172.25, 'expiry': '2017-11-30', 'strike': 25800.0, 'tick_size': 0.05,
      'lot_size': 40, 'instrument_type': 'PE', 'segment': 'NFO-OPT', 'exchange':
      'NFO'}
"""

print("""
      Creating kite context...
      """)
try:
    kite = KiteConnect(api_key, api_secret)
except Exception as e:
    print(e)
    sys.exit(1)

print("""
      Initializing websocket...
      """)
try:
    # Initialise.
    kws = WebSocket(api_key, access_token['public_token'],
                    access_token["user_id"])
except Exception as e:
    print(e)
    sys.exit(1)


def on_tick(tick, ws):
    # Callback for tick reception.
    # print('timestamp: {} tick: {}'.format(time.time(), tick))
    print('Sending {}'.format(json.dumps(tick)))
    socket.send_string(json.dumps(tick))


def on_connect(ws):
    # Callback for successful connection.
    # Subscribe to a list of instrument_tokens (RELIANCE and ACC
    # here).
    print("""
          Connected to zerodha...
          """)
    print("Subscribing to ...{}".format(instruments))
    print(type(instruments))
    # ws.subscribe([int(ce['instrument_token']), int(pe['instrument_token'])])
    ws.subscribe(instruments)

    # Set RELIANCE to tick in `full` mode.
    # ws.set_mode(ws.MODE_QUOTE, ce['instrument_token'])
    # ws.set_mode(ws.MODE_QUOTE, pe['instrument_token'])

# Assign the callbacks.
kws.on_tick = on_tick
kws.on_connect = on_connect

# To enable auto reconnect WebSocket connection in
# case of network failure
# - First param is interval between reconnection
# attempts in seconds.
# Callback `on_reconnect` is triggered on every
# reconnection attempt. (Default interval is 5
# seconds)
# - Second param is maximum number of retries before
# the program exits triggering `on_noreconnect`
# calback. (Defaults to 50 attempts)
# Note that you can also enable auto reconnection
# while initialising websocket.
# Example `kws = WebSocket("your_api_key",
# "your_public_token", "logged_in_user_id",
# reconnect=True, reconnect_interval=5,
# reconnect_tries=50)`
kws.enable_reconnect(reconnect_interval=5, reconnect_tries=50)

# Infinite loop on the main thread. Nothing after
# this will run.
# You have to use the pre-defined callbacks to
# manage subscriptions.
print("""
        Trying to connect...
        """)
kws.connect()
