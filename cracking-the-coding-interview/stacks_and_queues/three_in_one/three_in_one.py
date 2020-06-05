from stacks_and_queues.stack.stack import Stack, _Node


class ThreeInOneStack(Stack):
  """
  Memory manager for three stacks.
  """

  array = [None for _ in range(100)]


  def __init__(self):
    """
    Constructor.
    """
    
    super().__init__()


  def push(self, value):
    """
    Add value to stack.

    In:
    value (): Value of node added to stack.
    """

    i = 0
    while array[i] != None:
      i += 1

      if i == len(array):
        raise StackOverflowException()

    array[i] = _Node(value)
    array[i].next = self.head
    self.head = array[i]


  def pop(self):
    """
    Remove value from stack.

    Out:
    (): Value of the node removed from the top of the stack.
    """
    pass


  def is_empty(self):
    """
    See if the stack is empty.
    """


class StackOverflowException(Exception):
  """
  Too little stack memory exception.
  """

  def __init__(self):
    """
    Constructor.
    """

    super().__init__()
