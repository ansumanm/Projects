#!/Users/ansuman/Github/Projects/python/virtualenv/bin/python
#
"""
Update the configuration file with access token.
"""

from kiteconnect import KiteConnect
import sys
import ssl
import configparser

ssl._create_default_https_context = ssl._create_unverified_context

config = configparser.ConfigParser()
config.read('kuber.conf')

login_conf = config['Login Configuration']
api_key = login_conf['api_key']
api_secret = login_conf['api_secret']
request_token = login_conf['request_token']

try:
    kite = KiteConnect(api_key, api_secret)
except Exception as e:
    print(e)
    sys.exit(1)

try:
    token = kite.request_access_token(request_token, api_secret)
except Exception as e:
    print(e)
    sys.exit(1)

config['ACCESS INFO'] = token
with open('kuber.conf', 'w') as configfile:
    config.write(configfile)
