import pytest

from stacks_and_queues import Stack, Queue, EmptyStackException, EmptyQueueException


def test_empty_stack():
  """
  Exception raised when peeking empty stack.
  """

  stack = Stack()
  
  try:
    stack.peek()
  except EmptyStackException:
    assert True


def test_empty_queue():
  """
  Exception raised when peeking empty queue.
  """

  queue = Queue()

  try:
    queue.peek()
  except EmptyQueueException:
    assert True
