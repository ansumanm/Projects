#!/Users/ansuman/Github/Projects/python/virtualenv/bin/python
#
"""
Create a historical database of NSE stocks.
"""

from kiteconnect import KiteConnect
import sys
import ssl
import configparser
import webbrowser
# import urllib.request
# import urllib.response

ssl._create_default_https_context = ssl._create_unverified_context

config = configparser.ConfigParser()
config.read('kuber.conf')

login_conf = config['Login Configuration']
api_key = login_conf['api_key']
api_secret = login_conf['api_secret']

try:
    kite = KiteConnect(api_key, api_secret)
except Exception as e:
    print(e)
    sys.exit(1)

# print(kite.login_url())
webbrowser.open_new(kite.login_url())

"""
try:
    response = urllib.request.urlopen(kite.login_url())
except Exception as e:
    print(e)
    sys.exit(1)

print(response.geturl())

for instrument in (kite.instruments()):
    print(instrument)
    print("\n")
"""
