import math
  
with open("day10/day10_input.txt", "r") as f:
# with open("day10/day10_testin.txt", "r") as f:
  rows = [x for x in f.read().split('\n')]

def check_station(rows, sx, sy):
  lines = set()

  for y, row in enumerate(rows):
    for x, cell in enumerate(row):
      if cell != '#' or (x, y) == (sx, sy):
        continue
      
      dx = x - sx
      dy = y - sy

      gradient = abs(math.gcd(dx, dy)) # negative lines on the same slope

      lines.add((dx // gradient, dy // gradient))
  
  return lines

answer = (set(), 0, 0)
for y, row in enumerate(rows):
  for x, cell in enumerate(row):
    if cell != '#':
      continue

    lines = check_station(rows, x, y)
    if len(lines) > len(answer[0]):
      answer = (lines, x, y)

lines, x, y = answer

sorted_lines = sorted(lines, key=lambda l: math.atan2(l[0], l[1]), reverse=True)
dx, dy = sorted_lines[199]
x += dx
y += dy

while rows[y][x] != '#':
  x += dx
  y += dy

print(x, y, x * 100 + y)
