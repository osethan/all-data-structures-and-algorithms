import pytest
from linked_lists.linked_list.linked_list import LinkedList
from remove_dups import remove_dups


# Edge cases


def test_first_duplicate_kept(linked_list):
  """
  The first duplicate should be kept when removing duplicates.
  """

  values = [3, 2, 1, 2]
  for value in values:
    linked_list.prepend(value)

  expected = [2, 1, 3]
  actual = remove_dups(linked_list).values()

  assert actual == expected


def test_empty_linked_list(linked_list):
  """
  No changes made to empty linked list.
  """

  expected = []
  actual = remove_dups(linked_list).values()

  assert actual == expected


# Fixtures


@pytest.fixture
def linked_list():
  """
  Make LinkedList instance.
  """

  return LinkedList()
