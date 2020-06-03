import pytest
from is_unique import is_unique


# Expected passing cases


def test_unique_characters():
  """
  Characters seen as unique in string.
  """

  string = 'Python'

  expected = True
  actual = is_unique(string)

  assert actual == expected


# Expected failing cases


def test_not_unique_characters():
  """
  Characters not seen as unique in string.
  """

  string = 'java'

  expected = False
  actual = is_unique(string)

  assert actual == expected


# Edge cases


def test_uppercase():
  """
  Upper and lowercase characters count as the same character.
  """

  string = 'JAva'

  expected = False
  actual = is_unique(string)

  assert actual == expected


def test_empty_string():
  """
  Empty string has all unique characters.
  """

  string = ''

  expected = True
  actual = is_unique(string)

  assert actual == expected


def test_punctuation():
  """
  Punctuation characters aren't unique from each other.
  """

  string = 'Python::'

  expected = False
  actual = is_unique(string)

  assert actual == expected
