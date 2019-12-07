from day7_1_computer import Computer
from itertools import permutations

with open("day7_input.txt", "r") as f:
  inp = [int(x) for x in f.read().split(',')]

# inp = [int(x) for x in "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,\
# 33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0".split(',')]

maxout = 0
for comb in permutations([0, 1, 2, 3, 4], 5):
  c_in = 0
  for i in comb:
    c = Computer(inp, [i, c_in])
    c.run()
    c_in = c.outputs[0]
  
  maxout = max(c_in, maxout)

print(maxout)