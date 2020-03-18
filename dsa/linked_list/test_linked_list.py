import pytest

from linked_list import LinkedListNode


def test_str():
  """
  Linked list can be made into string form.
  """

  ll = LinkedListNode(2)
  ll.appendToTail(1)
  ll.appendToTail(2)
  ll.appendToTail(6)
  ll.appendToTail(6)

  expected = '[2] -> [1] -> [2] -> [6] -> [6]'
  actual = str(ll)

  assert actual == expected
