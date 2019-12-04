from collections import Counter

r = [153517, 630395]

def check_order(x):
  s = str(x)
  return ''.join(sorted(s)) == s

def has_double(x):
  s = str(x)
  count = Counter(s)

  return 2 in count.values()

val = 0
for i in range(r[0], r[1] + 1):
  if check_order(i):
    if has_double(i):
      val += 1

print(val)