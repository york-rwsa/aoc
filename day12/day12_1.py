from itertools import combinations
import re

with open('day12/day12_input.txt', 'r') as f:
  coors = re.findall(r'\w{1}=(-?\d+)', f.read())
  moons = [list(map(int, coors[i:i + 3])) for i in range(0, len(coors), 3)]
  velocs = [[0] * 3 for _ in range(len(moons))]

def calc_gravity(moons, velocs):
  for comb in combinations(moons, 2):
    i1 = moons.index(comb[0])
    i2 = moons.index(comb[1])

    for i, (v1, v2) in enumerate(zip(comb[0], comb[1])):
      if v1 > v2:
        val = -1
      elif v1 < v2:
        val = 1
      else:
        val = 0

      velocs[i1][i] += val
      velocs[i2][i] -= val
  
  for moon, veloc in zip(moons, velocs):
    for i, v in enumerate(veloc):
      moon[i] += v

print(moons, velocs)
for i in range(1000):
  calc_gravity(moons, velocs)
  print(moons, velocs)

kin = [sum(map(abs, v)) for v in velocs]
pot = [sum(map(abs, m)) for m in moons]

total = sum([k * p for k, p in zip(kin, pot)])
print(total)