import curses

with open('day8/day8_input.txt', 'r') as f:
  inp = f.read()

width = 25
height = 6
layerwidth = 25 * 6
layers = [inp[i:i + layerwidth] for i in range(0, len(inp), layerwidth)]

def render_layer(stdscr, width, height, layer):
  rows = [layer[i:i + width] for i in range(0, len(layer), width)]

  for y, row in enumerate(rows):
    for x, col in enumerate(row):
      if col == '2':
        continue
    
      stdscr.addstr(y + 3, x * 2 + 4, '  ', curses.color_pair(int(col) + 1))


def main(stdscr):
  stdscr.clear()
  curses.start_color()
  curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE)
  curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLUE)
  
  for layer in layers[::-1]:
    render_layer(stdscr, width, height, layer)
  
  stdscr.refresh()
  stdscr.getkey()

curses.wrapper(main)