
def permute(s, b = '', permutations = []):
  """
  Make all permutations of characters of a string.

  In:
  s (str): String to permute characters.
  b (str): String builder making permutation.
  permutations (list[str]): String permutations.

  Out:
  (list[str]): All string permutations.
  """

  if (len(s) == 0):
    permutations += [b]
    return permutations

  for i, char in enumerate(s):
    newStr = s[0 : i] + s[i + 1 :]
    newBuilder = b + char
    permutations = permute(newStr, newBuilder, permutations)

  return permutations


def palindrome(s):
  """
  String is a palindrome.
  """

  return s == s[-1::-1]


def permutation_palindrome(s):
  permutations = permute(s)
  for permutation in permutations:
    if palindrome(permutation):
      return True
  return False


if __name__ == "__main__":
  s = 'abc'
  permutations = permutation_palindrome(s)
  print(permutations)
