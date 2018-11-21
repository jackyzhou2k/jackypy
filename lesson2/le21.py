'''
Created on 2018年11月19日

@author: Jacky
'''
from random import randint
from pip._vendor.msgpack.fallback import xrange

data = [2,4,6,-3,-6,8,9]

res = []
for x in data:
    if x > 0:
        res.append(x)

print(res)

data =  [randint(-10,10) for _ in xrange(10)]
print(data)

def is_pos(x):
    return x>=0

res1= filter( is_pos , data)
res2=[x for x in data if x>=0]
print(list(res1))
print(res2)

d = {x:randint(60,100) for x in xrange(1,21)}
d90 = {k:v for k,v in d.items() if v>=90}
print(d)
print (d90)

s1 = set(data)
print(s1)
s2 = [x for x in s1 if x % 3 == 0]
print(s2)
