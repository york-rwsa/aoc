with open("day3_input.txt", "r") as f:
  inputs = f.read().split('\n')

class Line:
  def __init__(self, x1, y1, direction, length):
    self.x1 = x1
    self.y1 = y1
    self.d = direction
    self.length = length

  def points(self):
    if self.d == 'R':
      op = lambda i: (self.x1 + i, self.y1)
    elif self.d == 'L':
      op = lambda i: (self.x1 - i, self.y1)
    elif self.d == 'U':
      op = lambda i: (self.x1, self.y1 + i)
    elif self.d == 'D':
      op = lambda i: (self.x1, self.y1 - i)
    
    return [op(x) for x in range(1, self.length + 1)]

  def get_x2(self):
    if self.d == 'R':
      return self.x1 + self.length
    elif self.d == 'L':
      return self.x1 - self.length
    
    return self.x1

  def get_y2(self):
    if self.d == 'U':
      return self.y1 + self.length
    elif self.d == 'D':
      return self.y1 - self.length
    
    return self.y1

  def intersections(self, line):
    return list(set(self.points()).intersection(set(line.points())))
  
def genlines(instructions):
  lines = []
  x = 0
  y = 0
  for instruction in instructions:
    lines.append(Line(x, y, instruction[0], int(instruction[1:])))
    x = lines[-1].get_x2()
    y = lines[-1].get_y2()

  return lines

points = set()
for l in genlines(inputs[0].split(',')):
  points.update(l.points())

x = 0
y = 0
intersections = set()
for instruction in inputs[1].split(','):
  line = Line(x, y, instruction[0], int(instruction[1:]))
  x = line.get_x2()
  y = line.get_y2()

  intersects = points.intersection(line.points())
  intersections.update(intersects)

distances = [abs(i[0]) + abs(i[1]) for i in intersections]
print(min(distances))