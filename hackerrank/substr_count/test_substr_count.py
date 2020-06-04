import pytest
from hackerrank.substr_count.substr_count import substr_count

@pytest.mark.parametrize('n, s, expected', [
  (5, 'asasd', 7),
  (7, 'abcbaba', 10),
  (4, 'aaaa', 10)
])
def test_substr_count(n, s, expected):
  actual = substr_count(n, s)
  assert actual == expected