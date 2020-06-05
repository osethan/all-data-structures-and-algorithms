import pytest
from leetcode.longest_palindrome_substr.longest_palindrome_substr import longest_palindrome_substr

@pytest.mark.parametrize('str, expected', [
  ('babad', 'bab'),
  ('cbbd', 'bb')
])
def test_longest_palindrome_substr(str, expected):
  actual = longest_palindrome_substr(str)
  assert actual == expected