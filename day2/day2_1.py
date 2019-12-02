with open("day2_input.txt", "r") as f:
  inp = [int(x) for x in f.read().split(',')]

inp[1] = 12
inp[2] = 2

i = 0
while (inp[i] != 99):
  op = inp[i]
  d1 = inp[i + 1]
  d2 = inp[i + 2]
  dest = inp[i + 3]

  out = 0
  if op == 1:
    out = inp[d1] + inp[d2]
  elif op == 2:
    out = inp[d1] * inp[d2]

  inp[dest] = out

  i = i + 4

print(inp[0])