import pytest

from dsa.recursion.coin_change.coin_change import coin_change


@pytest.mark.parametrize('change, coins, expected', [
  (3, [1, 2], 2)
  # (4, [1, 2, 3], 4),
  # (10, [2, 5, 3, 6], 5)
])
def test_coin_change(change, coins, expected):
  actual = coin_change(change, coins)
  assert actual == expected
