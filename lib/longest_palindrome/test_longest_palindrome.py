import pytest

from longest_palindrome import longest_palindrome


@pytest.mark.parametrize('s, expected', [
  # Palindrome starts at start of string
  ('babad', 'bab'),
  # Palindrome starts at middle of string
  ('cbbd', 'bb'),
  # Palindrome is full string
  ('aba', 'aba')
])
def test_longest_palindrome(s, expected):
  """
  Longest palindrome substring found in string.

  In:
  s (str): String to search for palindrome substring.
  expected (str): Longest palindrome substring of string.
  """

  actual = longest_palindrome(s)

  assert actual == expected
