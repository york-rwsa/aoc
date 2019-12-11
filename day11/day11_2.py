from Computer import Computer
from collections import defaultdict

class HullPainter:
  def __init__(self, mem):
    self.c = Computer(mem)
    self.x = 0
    self.y = 0
    # (x, y): 1 if white else 0
    self.grid = defaultdict(lambda: 0)
    self.grid[0, 0] = 1
    self.direction = 0 # zero degrees up
    
  def run(self):
    painted = set()

    running = True
    while (running):
      self.c.inputs.append(self.grid[(self.x, self.y)])
      self.c.run()

      if not self.c.waiting_for_input or len(self.c.outputs) < 2:
        running = False
        break
      
      direction = self.c.outputs.pop()
      colour = self.c.outputs.pop()
      
      if self.grid[(self.x, self.y)] != colour:
        painted.add((self.x, self.y))
        self.grid[(self.x, self.y)] = colour

      self._move(direction)

    return painted

  def _move(self, d):
    d = -90 if d == 1 else 90
    self.direction = (self.direction + d) % 360

    if self.direction == 0:
      self.y += 1
    elif self.direction == 90:
      self.x += 1
    elif self.direction == 180:
      self.y -= 1
    elif self.direction == 270:
      self.x -= 1

with open("day11/day11_input.txt", "r") as f:
  inp = [int(x) for x in f.read().split(',')]

hp = HullPainter(inp)
painted = hp.run()
minx = 0
miny = 0
maxx = 0
maxy = 0 
for x, y in painted:
  minx = min(x, minx)
  miny = min(y, miny)
  maxx = max(x, maxx)
  maxy = max(y, maxy)

for y in range(maxy, miny - 1, -1):
  for x in range(maxx, minx - 1, -1):
    print('#' if hp.grid[(x, y)] == 1 else ' ', end='')
  print()