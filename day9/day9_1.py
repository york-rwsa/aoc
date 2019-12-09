from Computer import Computer

with open("day9/day9_input.txt", "r") as f:
  inp = [int(x) for x in f.read().split(',')]

# inp = [int(x) for x in "1102,34915192,34915192,7,4,7,99,0".split(',')]

c = Computer(inp, [2], True)
c.run()
print(c.outputs)