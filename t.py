import time
import os

try:
    import ntplib
    client = ntplib.NTPClient()
    response = client.request('gps1.gmrt.ncra.tifr.res.in')
    os.system('date ' + time.strftime('%m%d%H%M%Y.%S',time.localtime(response.tx_time)))
except:
    print('Could not sync with time server.')

print('Done.')
