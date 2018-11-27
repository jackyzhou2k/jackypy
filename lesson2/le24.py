'''
Created on 2018年11月27日

@author: Jacky
'''

from random import randint

data = {x: randint(60,100) for x in ('xyzabc')}
print(data)

print(sorted(data))

dt2 = sorted(zip(data.values(),data.keys()))
for d in dt2:
    print(d)

dt3 = data.items()
print(dt3)
dt4 = sorted(data.items(),key = lambda x:x[1],reverse=True)
print(dt4)
