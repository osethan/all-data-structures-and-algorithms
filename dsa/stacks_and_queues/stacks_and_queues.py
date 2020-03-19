
class Stack:
  """
  FILO Stack data structure.
  """

  class _StackNode:
    """
    FILO Stack node.
    """

    def __init__(self, value):
      """
      Stack node constructor.
      """

      self.value = value
      self.next = None

  
  def __init__(self):
    """
    Stack constructor.
    """

    self.top = None


  def pop(self):
    """
    See value of top node and remove top node.
    """
    
    if self.is_empty():
      raise EmptyStackException()

    node = self.top
    self.top = self.top.next
    return node.value


  def push(self, value):
    """
    Add new node with value to top of stack.
    """

    node = self._StackNode(value)
    node.next = self.top
    self.top = node


  def peek(self):
    """
    See value of top node.
    """
    
    if self.is_empty():
      raise EmptyStackException()

    return self.top.value


  def is_empty(self):
    """
    Find if stack is empty.
    """

    return not self.top


class Queue:
  """
  FIFO Queue data structure.
  """

  class _QueueNode:
    """
    Queue data structure node.
    """

    def __init__(self, value):
      """
      Queue node constructor.
      """

      self.value = value
      self.next = None


  def __init__(self):
    """
    Queue constructor.
    """

    self.front = None
    self.rear = None


  def add(self, value):
    """
    Add value to back of queue.

    In:
    value (): Any data to be the value of a new node.
    """

    node = self._QueueNode(value)
    if not self.front:
      self.front = node
      self.rear = node
      return
    
    self.rear.next = node
    self.rear = node


  def remove(self):
    """
    Remove value from front of queue.

    Out:
    (): Any data being the value of the removed front node.
    """
    
    if self.is_empty():
      raise EmptyQueueException()

    node = self.front
    self.front = self.front.next
    return node.value


  def peek(self):
    """
    See value at front of queue without removal.

    Out:
    (): Any data being the value of the front node.
    """
    
    if self.is_empty():
      raise EmptyQueueException()

    return self.front.value


  def is_empty(self):
    """
    Say whether the queue has no values.
    """

    return not self.front


class EmptyStackException(Exception):
  """
  Raised when trying to read empty stack.
  """
  pass


class EmptyQueueException(Exception):
  """
  Raised when trying to read empty queue.
  """
  pass
