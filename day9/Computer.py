from collections import defaultdict

class Computer():
  def __init__(self, mem, inputs=[], debug=False):
    self.ic = 0
    self.debug = debug
    # self.mem = defaultdict(lambda: 0, {i: x for i, x in enumerate(mem)})
    self.mem = mem[:]
    self.mem += [0] * 10000
    self.inputs = inputs
    self.waiting_for_input = False
    self.outputs = []
    self.relative_base = 0
    self.opcodes = {
      "01": {
        "name": "add",
        "op": self._add,
        "modes": "iio"
      },
      "02": {
        "name": "mul",
        "op": self._mul,
        "modes": "iio"
      },
      "03": {
        "name": "in", 
        "op": self._input,
        "modes": "o"
      },
      "04": {
        "name": "out", 
        "op": self._output,
        "modes": "i"
      },
      "05": {
        "name": "jnz", 
        "op": self._jump_true,
        "modes": "ii",
        "no_inc": True
      },
      "06": {
        "name": "jz", 
        "op": self._jump_false,
        "modes": "ii",
        "no_inc": True
      },
      "07": {
        "name": "lt",
        "op": self._less_than,
        "modes": "iio"
      },
      "08": {
        "name": "eq",
        "op": self._equals,
        "modes": "iio"
      },
      "09": {
        "name": "rel",
        "op": self._relative_base,
        "modes": "i"
      }
    }

  def run(self):
    status = True
    while(status):
      try:
        status = self._do_instruction()
      except:
        print(f"IC: {self.ic}, MEM: {self.mem[self.ic]}")
        raise

  def _do_instruction(self):
    # reset state
    self.waiting_for_input = False

    if self.mem[self.ic] == 99:
      return False

    opcode = str(self.mem[self.ic]).zfill(2)
    instruction = self.opcodes[opcode[-2:]]
    modes = opcode[:-2].zfill(len(instruction["modes"]))[::-1]
    operands = self._get_operands(modes, instruction["modes"])

    if self.debug:
      self._debug(instruction, modes, operands)

    if instruction["op"](operands, self.mem, self.ic) == False:
      return False

    if not instruction.get("no_inc", False):
      self.ic += len(modes) + 1

    return True

  def _debug(self, instruction, modes, operands):
    digits = len(str(len(self.mem)))
    max_operands = 3
    fstring = "{:0{digits}}: {:05} {:4} ".format(self.ic, self.mem[self.ic], instruction['name'], digits=digits)
    for i in range(max_operands):
      if i < len(operands):
        x = "{}"
        if modes[i] == "0":
          x = "[{}]"
        
        fstring += "{:>6}{}".format(x.format(self.mem[self.ic + i + 1]), (', ' if i < len(operands) - 1 else ''))
      else:
        fstring += "".rjust(8, ' ')
    
    fstring += ' ; '

    for i, op in enumerate(operands):
      fstring += "{:>8}{}".format(op, ', ' if i < len(operands) - 1 else '')
      
    print(fstring)

  def _get_operands(self, modes, m_format):
    operands = []
    for i, (mode, f) in enumerate(zip(modes, m_format), 1):
      if f == "i":
        if mode == "0":
          operands.append(self.mem[self.mem[self.ic + i]])
        elif mode == "1":
          operands.append(self.mem[self.ic + i])
        elif mode == "2":
          operands.append(self.mem[self.mem[self.ic + i] + self.relative_base])
        else:
          raise Exception("Unknown input mode")
      elif f == "o":
        if mode == "0":
          operands.append(self.mem[self.ic + i])
        elif mode == "2":
          operands.append(self.mem[self.ic + i] + self.relative_base)
        else:
          raise Exception("Unknown output mode")

    return operands

  def _add(self, operands, mem, ic):
    mem[operands[2]] = operands[0] + operands[1]
    
  def _mul(self, operands, mem, ic):
    mem[operands[2]] = operands[0] * operands[1]
  
  def _input(self, operands, mem, ic):
    if len(self.inputs) < 1:
      self.waiting_for_input = True
      return False
    
    mem[operands[0]] = self.inputs.pop(0)

  def _output(self, operands, mem, ic):
    self.outputs.append(operands[0])
    if self.debug:
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
    mem[operands[2]] = 1 if operands[0] < operands[1] else 0 

  def _equals(self, operands, mem, ic):
    mem[operands[2]] = 1 if operands[0] == operands[1] else 0
  
  def _relative_base(self, operands, mem, ic):
    self.relative_base += operands[0]
    

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
