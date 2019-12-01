from math import floor

with open("day1_input.txt") as f:
  print(sum([floor(int(x) / 3) - 2 for x in f]))
