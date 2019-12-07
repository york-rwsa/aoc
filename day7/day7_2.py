from day7_2_computer import Computer
from itertools import permutations

with open("day7_input.txt", "r") as f:
  inp = [int(x) for x in f.read().split(',')]

# inp = [int(x) for x in "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,\
# 27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5".split(',')]


maxout = 0
for comb in permutations([5, 6, 7, 8, 9], 5):
  computers = []
  for i in comb:
    c = Computer(inp, [i])
    computers.append(c)

  running = True
  next_input = [0]
  while running:
    for i, c in enumerate(computers):
      c.inputs += next_input

      c.run()
      if not c.waiting_for_input and i == 4:
        maxout = max(c.outputs[0], maxout)
        running = False
        break

      next_input = c.outputs[:]
      c.outputs = []

print(maxout)