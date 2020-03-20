from dsa.tree.tree import BinarySearchTreeNode


def minimal_tree(lst):
  """
  Create a BST with minimum height given a sorted list.

  In:
  lst (list): Sorted list whose values make a BST.

  Out:
  (BinarySearchTreeNode): BST node made with value of list.
  """

  # Recursive base case
  if len(lst) == 0:
    return None

  mid = len(lst) // 2
  node = BinarySearchTreeNode(lst[mid])

  # Make left node
  left = None
  if lst[0] == lst[mid]:
    left = minimal_tree([])
  else:
    left = minimal_tree(lst[0:mid])

  # Make right node
  right = None
  if lst[-1] == lst[mid]:
    right = minimal_tree([])
  else:
    right = minimal_tree(lst[mid + 1:])

  node.left = left
  node.right = right
  return node
