#!/Users/ansuman/Github/Projects/python/virtualenv/bin/python
#
# Simple urllib example

import sys
import ssl
import urllib.request

# To get over the following error:
# <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed
# (_ssl.c:748)>

ssl._create_default_https_context = ssl._create_unverified_context
url_link = "https://www.youtube.com/watch?v=OBo-RYUXZ04"
url_link = "https://www.youtube.com/watch?v=ezJO5wivg5Y"
url_link = 'https://www.facebook.com/plugins/video.php?href=https%3A%2F%2Fwww.facebook.com%2Fcapricorn.abhishek%2Fvideos%2F10211544326671751%2F'

if len(sys.argv) == 2:
    print('Usage: {} <video url> <video name>'.format(sys.argv[0]))
    sys.exit(0)

print('Downloading {}'.format(sys.argv[2]))
try:
    urllib.request.urlretrieve(sys.argv[1], sys.argv[2])
except Exception as e:
    # Got and exception
    print(e)

