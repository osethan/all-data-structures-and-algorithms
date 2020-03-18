import pytest

from lib.linked_list.linked_list import LinkedListNode
from remove_dups import remove_dups


def test_remove_dups(linked_lists):
  """
  Duplicate values of a linked list are removed.

  In:
  linked_lists (list[LinkedListNode]): Linked lists to have duplicates removed.
  """

  for i in range(len(linked_lists)):
    if i == 0:
      expected = '[2] -> [1] -> [6]'
      actual = str(remove_dups(linked_lists[i]))

      assert actual == expected


@pytest.fixture
def linked_lists():
  """
  List of sample Linked Lists.
  """

  # Some duplicates in linked list
  ll_a = LinkedListNode(2)
  ll_a.appendToTail(1)
  ll_a.appendToTail(2)
  ll_a.appendToTail(6)
  ll_a.appendToTail(6)

  return [ll_a]
