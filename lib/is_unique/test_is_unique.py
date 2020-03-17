import pytest

from is_unique import is_unique


@pytest.mark.parametrize('s, expected', [
  # Unique characters
  ('Python', True),
  # Not unique characters
  ('Java', False),
  # Not case sensitive
  ('JAva', False),
  # Empty string is unique
  ('', True)
])
def test_is_unique(s, expected):
  """
  String checked for all unique characters.

  In:
  s (str): The string being checked.
  expected (bool): Telling whether string has all unique characters.
  """

  actual = is_unique(s)

  assert actual == expected

