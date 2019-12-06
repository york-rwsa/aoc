class Node:
  def __init__ (self, name):
      self.children = []
      self.parents = []
      self.name = name

  def add_child (self, child):
    self.children.append(child)
  
  def add_parent (self, parent):
    self.parents.append(parent)

  def get_set (self):
    return set(self.children + self.parents)

  def __repr__ (self):
    return self.name

class Nodes:
  nodes = []

  def add_node(self, name, child):
    n = self.get_node(name)
    if not n:
      n = Node(name)
      self.nodes.append(n)
        
    c = self.get_node(child)
    if not c:
      c = Node(child)
      self.nodes.append(c)

    n.add_child(c)
    c.add_parent(n)


  def get_node(self, name):
    for node in self.nodes:
      if node.name == name:
        return node
    
    return False

def search(nodes, start, aim):
  queue = [(start, [start])]

  while queue:
    (node, path) = queue.pop(0)

    for next in node.get_set() - set(path):
      if next == aim:
        yield path + [next]
      else:
        queue.append((next, path + [next]))

# inputs = """COM)B
# B)C
# C)D
# D)E
# E)F
# B)G
# G)H
# D)I
# E)J
# J)K
# K)L
# K)YOU
# I)SAN"""

with open('day6_input.txt', 'r') as f:
  inputs = f.read()

orbits = {x[1]: x[0] for x in map(lambda s: s.split(')'), inputs.split('\n'))}
nodes = Nodes()

for key, val in orbits.items():
  nodes.add_node(key, val)

start = nodes.get_node('YOU')
aim = nodes.get_node('SAN')

path = list(next(search(nodes, start, aim)))
print(len(path) - 3, path)