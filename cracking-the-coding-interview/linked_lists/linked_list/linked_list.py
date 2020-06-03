
class LinkedList():
  """
  Linked List data structure.
  """

  def __init__(self):
    """
    Constructor.
    """

    self.head = None


  def prepend(self, value):
    """
    Add new node with value to start of linked list.

    In:
    value (): Becomes value of linked list node.
    """

    node = _Node(value)
    node.next = self.head
    self.head = node


  def values(self):
    """
    See all values of linked list.

    Out:
    (list): Values of linked list in order.
    """

    values = []
    current = self.head
    
    while current:
      values.append(current.value)
      current = current.next

    return values


class _Node():
  """
  Singly Linked List node data structure.
  """

  def __init__(self, value):
    """
    Constructor.
    """

    self.value = value
    self.next = None
