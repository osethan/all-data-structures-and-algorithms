
def coin_change(change, coins):
  return find_coin_change(change, coins)


def find_coin_change(change, coins, count = 0, memo = {}):
  # Recursion base case
  if count == change:
    return 1
  elif count > change:
    return 0

  for coin in coins:
    # Memoization case
    if count not in memo:
      memo[count] = -1
    new_count = count + coin
    if new_count in memo:
      memo[count] += memo[new_count]
    else:
      memo[count] += find_coin_change(change, coins, new_count, memo)

  print(count, memo)
  return memo[count]


if __name__ == "__main__":
  change = 3
  coins = [1, 2]
  coin_change(change, coins)
