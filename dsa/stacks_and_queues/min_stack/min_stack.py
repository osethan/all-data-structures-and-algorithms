from dsa.stacks_and_queues.stacks_and_queues import Stack


class MinStack(Stack):
  
  def __init__(self):
    super().__init__()
    self.min_stack = Stack()


  def push(self, value):
    super().push(value)
    if self.min_stack.is_empty():
      self.min_stack.push(value)
    else:
      min_val = self.min_stack.peek()
      if value < min_val:
        self.min_stack.push(value)
      else:
        self.min_stack.push(min_val)


  def pop(self):
    value = super().pop()
    self.min_stack.pop()
    return value


  def min(self):
    return self.min_stack.peek()
