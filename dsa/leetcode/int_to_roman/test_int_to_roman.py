import pytest

from dsa.leetcode.int_to_roman.int_to_roman import int_to_roman


@pytest.mark.parametrize('num, expected', [
  # Expected successes
  (3, 'III'),
  (4, 'IV'),
  (9, 'IX'),
  (50, 'L'),
  (58, 'LVIII'),
  (1994, 'MCMXCIV')
])
def test_int_to_roman(num, expected):
  """
  Convert and integer to a roman number.
  """

  actual = int_to_roman(num)
  assert actual == expected
