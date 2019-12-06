# inputs = """COM)B
# B)C
# C)D
# D)E
# E)F
# B)G
# G)H
# D)I
# E)J
# J)K
# K)L"""

with open('day6_input.txt', 'r') as f:
  inputs = f.read()

orbits = {x[1]: x[0] for x in map(lambda s: s.split(')'), inputs.split('\n'))}

count = 0
for key, val in orbits.items():
  count += 1
  while val != 'COM':
    val = orbits.get(val, False)
    if not val:
      print(f"{key}, {val}")
  
    count += 1

print(count)
