'''
Created on 2018年11月27日

@author: Jacky
'''
from collections import OrderedDict
from time import time
from random import randint
from pip._vendor.distlib.compat import raw_input
from pip._vendor.msgpack.fallback import xrange

d = OrderedDict()
d['Jacky']=(1,20)
d['Tracy']=(1,22)
d['Dora']=(2,20)
for k in d:
    print(k)

players = list('ABCDEFGH')
d = OrderedDict()
start = time()

for i in xrange(8):
    raw_input()
    p = players.pop(randint(0,7-i))
    end = time()
    print(i+1,p,end - start)
    d[p]=(i+1,end - start)

print()
print('='*20)
for k in d:
    print(k,d[k])
