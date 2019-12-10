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
  
  return len(lines)

answer = 0
for y, row in enumerate(rows):
  for x, cell in enumerate(row):
    if cell != '#':
      continue

    answer = max(answer, check_station(rows, x, y))

print(answer)
