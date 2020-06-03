
class Stack():
  """
  Stack data structure.
  """

  def __init__(self):
    """
    Constructor.
    """

    self.head = None
  

  def push(self, value):
    """
    Add value to stack.

    In:
    value (): Value of node to add to top of stack.
    """
    pass


  def pop(self):
    """
    Remove head of stack.

    Out:
    (): Value of the node removed from the top of the stack.
    """
    
    if self.is_empty():
      raise EmptyStackException()


    value = self.head.value
    self.head


  def peek(self):
    """
    See the head of the stack.

    Out:
    (): Value of the node at the top of the stack.
    """
    
    if self.is_empty():
      raise EmptyStackException()

    return self.head.value


  def is_empty(self):
    """
    See if the stack has no nodes.

    Out:
    (boolean): Whether the stack is empty.
    """
    
    return self.head == None


class _Node():
  """
  Stack data structure node.
  """

  def __init__(self, value):
    """
    Constructor.
    """

    self.value = value
    self.next = None


class EmptyStackException(Exception):
  """
  Found when accessing nodes of an empty stack.
  """

  def __init__(self):
    """
    Constructor.
    """

    super().__init__()
