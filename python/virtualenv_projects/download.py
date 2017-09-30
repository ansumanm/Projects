#!/Users/ansuman/Github/Projects/python/virtualenv/bin/python
#
# Simple urllib example

import ssl
import urllib.request

# To get over the following error:
# <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed
# (_ssl.c:748)>

ssl._create_default_https_context = ssl._create_unverified_context
url_link = 'https://www.youtube.com/view_video.php?viewkey=ph599108d31093e'
try:
    urllib.request.urlretrieve(url_link, 'arjunreddy.mp4')
except Exception as e:
    # Got and exception
    print(e)

# Multi line print Ex.
# print('''
#       This is an example of multiline print.
#       Hello multiline print
#       Done.
#      ''')
