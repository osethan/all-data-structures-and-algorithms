import pytest
from leetcode.max_area.max_area import max_area

@pytest.mark.parametrize('heights, expected', [
  ([1,8,6,2,5,4,8,3,7], 49)
])
def test_max_area(heights, expected):
  actual = max_area(heights)
  assert actual == expected