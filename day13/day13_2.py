import curses
import time
from Computer import Computer
from collections import defaultdict

class Arcade:
  tiles = [
    lambda scr, x, y: scr.addstr(y, x * 2, '  ', curses.color_pair(1)),
    lambda scr, x, y: scr.addstr(y, x * 2, '  ', curses.color_pair(2)),
    lambda scr, x, y: scr.addstr(y, x * 2, '  ', curses.color_pair(3)),
    lambda scr, x, y: scr.addstr(y, x * 2, '__', curses.color_pair(4)),
    lambda scr, x, y: scr.addstr(y, x * 2, '  ', curses.color_pair(5)),
  ]

  def __init__(self, mem, stdscr):
    self.c = Computer(mem)
    self.screen = defaultdict(lambda: 0)
    self.stdscr = stdscr
    self.score = 0
    self.paddle = 0
    self.ball = 0

  def run(self):
    running = True
    while(running):
      while(len(self.c.outputs) < 3):
        ret = self.c._do_instruction()

        if self.c.waiting_for_input:
          # time.sleep(0.01)
          if self.ball > self.paddle:
            i = 1
          elif self.ball < self.paddle:
            i = -1
          else:
            i = 0
          
          self.c.inputs.append(i)
        elif not ret:
          running = False
          break

      if running == False:
        break
      tile = self.c.outputs.pop()
      y = self.c.outputs.pop()
      x = self.c.outputs.pop()

      if x == -1 and y == 0:
        self.score = tile
        self.stdscr.addstr(1, 4, f'SCORE: {self.score}', curses.color_pair(0)),
      else:
        if tile == 3:
          self.paddle = x
        elif tile == 4:
          self.ball = x
        
        self.draw_tile(x, y, tile)
  
  def draw_tile(self, x, y, tile):
    self.screen[(x, y)] = tile
    self.tiles[tile](self.stdscr, x + 2, y + 2)
    self.stdscr.refresh()

  def draw(self):
    for i in range(0, len(self.c.outputs), 3):
      x = self.c.outputs[i]
      y = self.c.outputs[i + 1]
      tile = self.c.outputs[i + 2]

      self.screen[(x, y)] = tile


with open("day13/day13_input.txt", "r") as f:
  inp = [int(x) for x in f.read().split(',')]

def main(stdscr):
  stdscr.clear()
  curses.start_color()
  curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE)
  curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLUE)
  curses.init_pair(3, curses.COLOR_RED, curses.COLOR_RED)
  curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_BLUE)
  curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_GREEN)
  
  a = Arcade(inp, stdscr)
  a.c.mem[0] = 2
  a.run()

  stdscr.refresh()
  stdscr.getkey()

curses.wrapper(main)