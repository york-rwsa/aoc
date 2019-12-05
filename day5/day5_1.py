class Computer():
  opcodes = {}
  mem = []
  ic = 0

  def __init__(self, mem):
    self.mem = mem
    self.opcodes = {
      "01": {
        "name": "Add",
        "op": self._add,
        "n_operands": 3
      },
      "02": {
        "name": "Mul",
        "op": self._mul,
        "n_operands": 3
      },
      "03": {
        "name": "Input", 
        "op": self._input,
        "n_operands": 1
      },
      "04": {
        "name": "Output", 
        "op": self._output,
        "n_operands": 1
      }
    }

  def run(self):
    while(self.mem[self.ic] != 99):
      try:
        self._do_instruction()
      except:
        print(f"{self.ic=}, {self.mem[self.ic]}")
        raise

  def _do_instruction(self):
    opcode = str(self.mem[self.ic]).zfill(2)
    instruction = self.opcodes[opcode[-2:]]
    modes = opcode[:-2].zfill(instruction["n_operands"])[::-1]

    instruction["op"](self._get_operands(modes), self.mem, self.ic)
    self.ic += len(modes) + 1

  def _get_operands(self, modes):
    operands = []
    for i, mode in enumerate(modes, 1):
      if mode == "0":
        operands.append(self.mem[self.mem[self.ic + i]])
      elif mode == "1":
        operands.append(self.mem[self.ic + i])
    
    return operands

  def _add(self, operands, mem, ic):
    mem[mem[ic + 3]] = operands[0] + operands[1]
    
  def _mul(self, operands, mem, ic):
    mem[mem[ic + 3]] = operands[0] * operands[1]
  
  def _input(self, operands, mem, ic):
    # spoof passing 1
    mem[mem[ic + 1]] = 1 

  def _output(self, operands, mem, ic):
    print(ic, operands[0])

# # add
# c = Computer([1101, 100, -5, 5, 99, 0])
# c.run()
# print(c.mem)

# # mul
# c = Computer([1002, 5, 3, 5, 99, 32])
# c.run()
# print(c.mem)

# # output
# c = Computer([104, 5, 4, 2, 99])
# c.run()
# print(c.mem)

with open("day5_input.txt", "r") as f:
  inp = [int(x) for x in f.read().split(',')]

c = Computer(inp)
c.run()