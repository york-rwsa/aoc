from Computer import Computer
from collections import defaultdict

class Arcade:
  def __init__(self, mem):
    self.c = Computer(mem)
    self.screen = defaultdict(lambda: 0)

  def run(self):
    self.c.run()

  def draw(self):
    for i in range(0, len(self.c.outputs), 3):
      x = self.c.outputs[i]
      y = self.c.outputs[i + 1]
      tile = self.c.outputs[i + 2]

      self.screen[(x, y)] = tile


with open("day13/day13_input.txt", "r") as f:
  inp = [int(x) for x in f.read().split(',')]

a = Arcade(inp)
a.run()
a.draw()

print(list(a.screen.values()).count(2))
