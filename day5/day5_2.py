class Computer():
  opcodes = {}
  mem = []
  ic = 0
  input_counter = 0
  inputs = []

  def __init__(self, mem, inputs=[]):
    self.mem = mem
    self.inputs = inputs
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
      },
      "05": {
        "name": "jump-if-true", 
        "op": self._jump_true,
        "n_operands": 2,
        "no_inc": True
      },
      "06": {
        "name": "jump-if-false", 
        "op": self._jump_false,
        "n_operands": 2,
        "no_inc": True
      },
      "07": {
        "name": "Less Than",
        "op": self._less_than,
        "n_operands": 3
      },
      "08": {
        "name": "Equals",
        "op": self._equals,
        "n_operands": 3
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

    if not instruction.get("no_inc", False):
      self.ic += len(modes) + 1

  def _inc_ic(self, width):
    self.ic += width

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
    mem[mem[ic + 1]] = self.inputs[self.input_counter]
    self.input_counter += 1

  def _output(self, operands, mem, ic):
    print(ic, operands[0])
  
  def _jump_true(self, operands, mem, ic):
    if operands[0] != 0:
      self.ic = operands[1]
    else:
      self.ic += len(operands) + 1

  def _jump_false(self, operands, mem, ic):
    if operands[0] == 0:
      self.ic = operands[1]
    else:
      self.ic += len(operands) + 1
  
  def _less_than(self, operands, mem, ic):
    mem[mem[ic + 3]] = 1 if operands[0] < operands[1] else 0 

  def _equals(self, operands, mem, ic):
    mem[mem[ic + 3]] = 1 if operands[0] == operands[1] else 0 
    

def tests():
  # add
  c = Computer([1101, 100, -5, 5, 99, 0])
  c.run()
  print(c.mem)

  # mul
  c = Computer([1002, 5, 3, 5, 99, 32])
  c.run()
  print(c.mem)

  # input
  c = Computer([3, 5, 3, 6, 99, 0, 6], [123, 321])
  c.run()
  print(c.mem)

  # output
  c = Computer([104, 5, 4, 2, 99])
  c.run()
  print(c.mem)

  # jump true
  c = Computer([1105, 1, 6, 0, 0, 0, 104, 1, 99])
  c.run()
  c = Computer([1105, 0, 6, 104, 0, 99, 104, 1, 99])
  c.run()

  # jump false
  c = Computer([1106, 0, 6, 0, 0, 0, 104, 1, 99])
  c.run()
  c = Computer([1106, 1, 6, 104, 0, 99, 104, 1, 99])
  c.run()

  # less than
  c = Computer([1107, 1, 2, 9, 1107, 2, 1, 10, 99, -1, -1])
  c.run()
  print(c.mem)

  # eq
  c = Computer([1108, 2, 2, 9, 1108, 2, 1, 10, 99, -1, -1])
  c.run()
  print(c.mem)

with open("day5_input.txt", "r") as f:
  inp = [int(x) for x in f.read().split(',')]

c = Computer(inp, [5])
c.run()