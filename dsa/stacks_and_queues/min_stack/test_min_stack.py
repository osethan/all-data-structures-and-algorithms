import pytest

from dsa.stacks_and_queues.stacks_and_queues import EmptyStackException
from min_stack import MinStack


def test_heighten_min_stack():
  min_stack = MinStack()
  values_mins = [(4, 4), (6, 4), (2, 2), (1, 1), (5, 1)]
  for value_min in values_mins:
    min_stack.push(value_min[0])
    expected = value_min[1]
    actual = min_stack.min()
    assert actual == expected


def test_shorten_min_stack():
  min_stack = MinStack()
  values_mins = [(4, 4), (6, 4), (2, 2), (1, 1), (5, 1)]
  
  for value_min in values_mins:
    min_stack.push(value_min[0])
    
  for value_min in values_mins[::-1]:
    expected = value_min[1]
    actual = min_stack.min()
    assert actual == expected
    min_stack.pop()


def test_empty_min_stack():
  min_stack = MinStack()
  try:
    min_stack.peek()
  except EmptyStackException:
    assert True
