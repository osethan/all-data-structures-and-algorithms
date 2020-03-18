
class BinaryTreeNode:
  """
  Binary Tree data structure.
  """

  def __init__(self, value):
    """
    Binary Tree constructor.

    In:
    value (): Any data to be the value of the binary tree node.
    """

    self.value = value
    self.left = None
    self.right = None


class BinarySearchTreeNode(BinaryTreeNode):
  """
  Binary Search Tree data structure.
  """

  def __init__(self, value):
    """
    Binary Search Tree constructor.

    In:
    value (): Any data to be the value of the binary search tree node.
    """

    super().__init__()
