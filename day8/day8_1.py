with open('day8/day8_input.txt', 'r') as f:
  inp = f.read()

width = 25
height = 6
layerwidth = 25 * 6
layers = [inp[i:i + layerwidth] for i in range(0, len(inp), layerwidth)]

minzeros = None
ans = None
for layer in layers:
  count = layer.count('0')
  
  if minzeros is not None and count > minzeros:
    continue

  minzeros = count
  ans = layer.count('1') * layer.count('2')

print(ans)