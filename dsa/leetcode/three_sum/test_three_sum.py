import pytest

from dsa.leetcode.three_sum.three_sum import three_sum


@pytest.mark.parametrize('lst, expected', [
  ([-1, 0, 1, 2, -1, -4], [
    [-1, 0, 1],
    [-1, -1, 2]
  ])
])
def test_three_sum(lst, expected):

  actual = three_sum(lst)
  assert actual == expected
