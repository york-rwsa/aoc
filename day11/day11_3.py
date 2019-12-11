from Computer import Computer
from collections import defaultdict
import time
import curses

class HullPainter:
  def __init__(self, mem, stdscr=None, xoffset=None, yoffset=None):
    self.c = Computer(mem)
    self.x = 0
    self.y = 0
    # (x, y): 1 if white else 0
    self.grid = defaultdict(lambda: 0)
    self.grid[0, 0] = 1
    self.direction = 0 # zero degrees up
    
    self.stdscr = stdscr
    self.xoffset = xoffset
    self.yoffset = yoffset

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
      if self.stdscr:
        self._paint(self.x, self.y, colour)

      self._move(direction)


    return painted

  def _move(self, d):
    d = -90 if d == 1 else 90
    self.direction = (self.direction + d) % 360

    if self.direction == 0:
      self.y -= 1
    elif self.direction == 90:
      self.x -= 1
    elif self.direction == 180:
      self.y += 1
    elif self.direction == 270:
      self.x += 1
    
  def _paint(self, x, y, colour):
    if x < -self.xoffset or y < -self.yoffset:
      return
    
    self.stdscr.addstr(y + self.yoffset, x + self.xoffset, ' ', curses.color_pair(colour + 1))
    self.stdscr.refresh()
    time.sleep(0.05)

      

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

xoffset = (abs(minx) if minx < 0 else 0) + 1
yoffset = (abs(miny) if miny < 0 else 0) + 1

def main(stdscr):
  stdscr.clear()
  curses.start_color()
  curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE)
  curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLUE)
  
  for y in range(maxy, miny - 1, -1):
    for x in range(maxx + 3, minx - 1, -1):
      stdscr.addstr(y + yoffset, x + xoffset, ' ', curses.color_pair(1))
  stdscr.refresh()

  hp2 = HullPainter(inp, stdscr, xoffset, yoffset)
  hp2.run()
  stdscr.refresh()
  stdscr.getkey()

curses.wrapper(main)