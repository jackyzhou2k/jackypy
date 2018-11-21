'''
Created on 2018年11月21日

@author: Jacky
'''
from random import randint
from collections import Counter
from pip._vendor.msgpack.fallback import xrange
import re

data = [randint(60,100) for _ in xrange(30)]

dt1 = dict.fromkeys(data, 0)
print(dt1)
for x in data:
    dt1[x]+=1
print(dt1)

lst = sorted(dt1.items(),key = lambda x:x[1],reverse=True)
print(lst)

cnt1 = Counter(data)
print(cnt1)
print (cnt1.most_common(3))

txt = open('new22.txt').read()
lst2 = re.split('\W+', txt)
cnt2 = Counter(lst2)
print(lst2)
print(cnt2.most_common(20))