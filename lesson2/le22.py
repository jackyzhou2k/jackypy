'''
Created on 2018年11月20日

@author: Jacky
'''
from pip._vendor.msgpack.fallback import xrange
from collections import namedtuple
name,age,sex = xrange(3)
s1=('Jacky',38,'Male')
print (s1[name] + str(s1[age]) + s1[sex])

Student = namedtuple('Student', ['name','age','sex'])
s2 = Student('Tracy',39,'Female')
print(s2.name+str(s2.age)+s2.sex)