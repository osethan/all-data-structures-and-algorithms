import pytest
from interview.can_jump.can_jump import can_jump

@pytest.mark.parametrize('lst, expected', [
  ([2,3,1,1,4], True),
  ([3,2,1,0,4], False)
])
def test_can_jump(lst, expected):
  actual = can_jump(lst)
  assert actual == expected
