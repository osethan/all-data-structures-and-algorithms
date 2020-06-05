import pytest

from dsa.arrays_and_strings.permutation_palindrome.permutation_palindrome import permutation_palindrome


@pytest.mark.parametrize('s, expected', [
  ('aab', True),
  ('abc', False)
])
def test_permutation_palindrome(s, expected):
  actual = permutation_palindrome(s)
  assert actual == expected
