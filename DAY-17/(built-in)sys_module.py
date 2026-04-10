'''
import sys

print(sys.argv)
print(sys.exit())
print(sys.path)
print(sys.version)
print(sys.exit())
print('start')
print(sys.exit())
print('end')
-----------------------------------
import platform

print(platform.system())
print(platform.release())
print(platform.processor())
------------------------------------
import math

print(math.pi)
print(math.e)
print(math.sqrt(36))
print(math.pow(3,4))
print(math.ceil(12.000001))
print(math.floor(12.9999))
print(round(12.9999))
print(abs(-12))
print(math.fabs(-12))
print(math.factorial(5))
print(math.gcd(-12,8))
print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))

-------------------------------------

import collections

s='python programming'
l=[1,2,3,12,34,1,2,3,4,3,4,2,12]
r = 'this is that that is this'.split()

res = collections.Counter(s)
res1 = collections.Counter(l)
res2 = collections.Counter(r)
print(res)
print(res1)
print(res2)
------------------------------------------
res= collections.defaultdict(int) ## printing dict with default values
for i in s:
    res[i] = res[i] +1
print(res)
--------------------------------------------

import collections

q = collections.deque([])
## deque is double-ended queues for fast append/pops
q.append(20)
q.append(30)
q.append(60)
q.append(70)
q.append(90)
q.popleft()
q.popleft()
q.popleft()
q.append(10)
q.append(40)
print(q)

--------------------------------------------
'''
from itertools import combinations, permutations
s='abc'
print(list(combinations(s,3)))
print(list(permutations(s,3)))

































































