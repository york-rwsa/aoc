with open("day3_input.txt", "r") as f:
  inputs = f.read().split('\n')

# inputs = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split('\n')

def gen_wire(wirein):
  out = {}
  x = 0
  y = 0
  steps = 0

  for w in wirein:
    d = w[0]
    l = int(w[1:])

    if d == 'R':
      op = lambda x, y: (x + 1, y)
    elif d == 'L':
      op = lambda x, y: (x - 1, y)
    elif d == 'U':
      op = lambda x, y: (x, y + 1)
    elif d == 'D':
      op = lambda x, y: (x, y - 1)

    for i in range(l):
      x, y = op(x, y)
      steps += 1
      out[(x, y)] = steps

  return out

a = gen_wire(inputs[0].split(','))
b = gen_wire(inputs[1].split(','))

intersections = set(a.keys()).intersection(b.keys())
print('part 1: ', min([abs(i[0]) + abs(i[1]) for i in intersections]))

distances = [a[i] + b[i] for i in intersections]
print('part 2: ', min(distances))
