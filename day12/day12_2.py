from copy import deepcopy
from math import gcd
from itertools import combinations
from functools import reduce
import re

with open('day12/day12_input.txt', 'r') as f:
  coors = re.findall(r'\w{1}=(-?\d+)', f.read())
  moons = [[[int(x), 0] for x in coors[i:i + 3]] for i in range(0, len(coors), 3)]

def lcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)

def calc(moons, i):
  for comb in combinations(moons, 2):
    v1 = comb[0][i]
    v2 = comb[1][i]
    
    val = 0
    if v1[0] < v2[0]:
      val = 1
    elif v1[0] > v2[0]:
      val = -1
     
    v1[1] += val
    v2[1] -= val
  
  for moon in moons:
    moon[i][0] += moon[i][1]
  
steps = []
for x in range(3):
  new_state = deepcopy(moons)

  i = 0
  while(True):
    calc(new_state, x)
    i += 1
    if new_state == moons:
      steps.append(i)
      break


print(steps, lcm(steps))