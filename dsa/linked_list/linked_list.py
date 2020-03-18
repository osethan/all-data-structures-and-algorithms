class LinkedListNode:
  """
  Node of Linked List data structure.
  """

  def __init__(self, value):
    """
    Linked List Node constructor.

    In:
    value (): Any data to be the value of the node.
    """

    self.value = value
    self.next = None


  def __str__(self):
    """
    String form of linked list.
    """

    ll_str = ''
    current = self
    while current:
      ll_str += f'[{current.value}]'
      if current.next:
        ll_str += ' -> '
      current = current.next
    return ll_str

  
  def appendToTail(self, value):
    """
    Add a new node with a value after all next nodes.

    In:
    value (): Any data to be the value of the new node.
    """

    node = LinkedListNode(value)
    current = self
    while current.next:
      current = current.next
    current.next = node
