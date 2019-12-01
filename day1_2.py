from math import floor

def fuel_required(mass):
  req = floor(mass / 3) - 2
  if req < 1:
    return 0
  
  return req + fuel_required(req)

with open("day1_input.txt") as f:
  print(sum([fuel_required(int(x)) for x in f]))
