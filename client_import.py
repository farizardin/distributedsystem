from zatt.client import DistributedDict
import time
starttime = time.time()
d = DistributedDict('127.0.0.1', 8660)
print('port: 8660')
print(d['key'])
endtime = time.time()
print(endtime - starttime)
