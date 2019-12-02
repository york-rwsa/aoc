def compute(i1, i2, intcode):
  ic = intcode[:]
  ic[1] = i1
  ic[2] = i2

  i = 0
  while (ic[i] != 99):
    op = ic[i]
    d1 = ic[i + 1]
    d2 = ic[i + 2]
    dest = ic[i + 3]

    out = 0
    if op == 1:
      out = ic[d1] + ic[d2]
    elif op == 2:
      out = ic[d1] * ic[d2]

    ic[dest] = out

    i = i + 4

  return ic[0]

with open("day2_input.txt", "r") as f:
  inp = [int(x) for x in f.read().split(',')]

for i in range(0, 100):
  for j in range(0, 100):
    out = compute(i, j, inp)
    if out == 19690720:
      print(100 * i + j)
      break