import pytest
from leetcode.three_sum.three_sum import three_sum

@pytest.mark.parametrize('nums, expected', [
  ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]])
])
def test_three_sum(nums, expected):
  actual = three_sum(nums)
  print(actual)
  assert actual == expected