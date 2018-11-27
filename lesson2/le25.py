from random import randint,sample
from test import test_dictviews
from _functools import reduce

s1 = {x:randint(1,4) for x in sample('xyzabc',randint(3,6))}
s2 = {x:randint(1,4) for x in sample('xyzabc',randint(3,6))}
s3 = {x:randint(1,4) for x in sample('xyzabc',randint(3,6))}
print(s1,s2,s3)
res = map(dict.keys,[s1,s2,s3])
for d in res:
    print(d)
res2 = reduce(lambda x,y:x&y , map(dict.keys,[s1,s2,s3]))
print(res2)