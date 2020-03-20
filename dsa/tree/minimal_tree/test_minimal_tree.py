import pytest

from dsa.tree.minimal_tree.minimal_tree import minimal_tree
from dsa.tree.tree import BinarySearchTreeNode


def test_minimal_tree_left_and_right():
  """
  BST made with list which at mid has left value and right value.
  """

  bst_node = BinarySearchTreeNode(2)
  bst_node.left = BinarySearchTreeNode(1)
  bst_node.right = BinarySearchTreeNode(3)

  lst = [1, 2, 3]
  actual = minimal_tree(lst)

  assert actual.value == bst_node.value
  assert actual.left.value == bst_node.left.value
  assert actual.right.value == bst_node.right.value


def test_minimal_tree_left_no_right():
  """
  BST made with list which at mid has left value but no right value.
  """

  bst_node = BinarySearchTreeNode(2)
  bst_node.left = BinarySearchTreeNode(1)

  lst = [1, 2]
  actual = minimal_tree(lst)

  assert actual.value == bst_node.value
  assert actual.left.value == bst_node.left.value
  assert actual.right == bst_node.right


def test_minimal_tree_no_left_no_right():
  """
  BST made with list which at mid has no left value and no right value.
  """

  bst_node = BinarySearchTreeNode(2)

  lst = [2]
  actual = minimal_tree(lst)

  assert actual.value == bst_node.value
  assert actual.left == bst_node.left
  assert actual.right == bst_node.right


def test_minimal_tree_many_nodes():
  """
  BST made with list of many values.
  """

  bst_node = BinarySearchTreeNode(3)
  bst_node.left = BinarySearchTreeNode(2)
  bst_node.right = BinarySearchTreeNode(5)
  bst_node.left.left = BinarySearchTreeNode(1)
  bst_node.right.left = BinarySearchTreeNode(4)

  lst = [1, 2, 3, 4, 5]
  actual = minimal_tree(lst)

  assert actual.value == bst_node.value
  assert actual.left.value == bst_node.left.value
  assert actual.right.value == bst_node.right.value
  assert actual.left.left.value == bst_node.left.left.value
  assert actual.left.right == bst_node.left.right
  assert actual.right.left.value == bst_node.right.left.value
  assert actual.right.right == bst_node.right.right
