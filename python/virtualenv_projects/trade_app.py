#!/usr/local/bin/python3
# Trading app.

import ssl
from nsetools import Nse
from pprint import pprint

# To get over the following error:
# <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate
# verify failed (_ssl.c:748)>
ssl._create_default_https_context = ssl._create_unverified_context

nse = Nse()
q = nse.get_quote('infy')
print(type(q))
pprint(q)

# nifty_quote = nse.get_index_quote('NIFTY 50')
# banknifty_quote = nse.get_index_quote('NIFTY BANK')

# pprint(nifty_quote)
# pprint(banknifty_quote)

# Write OHLC data to a file.

"""
try:
    all_stock_codes = nse.get_stock_codes()
    # pprint(all_stock_codes)

    for stock_code, desc in all_stock_codes.items():
        print('stock_code = ', stock_code)
        print('description = ', desc)

        if nse.is_valid_code(stock_code):
            quote = nse.get_quote(stock_code)
            # Write OHLC data to a file.

except Exception as e:
    print(e)
"""


# index_codes = nse.get_index_list()
# pprint(index_codes)
