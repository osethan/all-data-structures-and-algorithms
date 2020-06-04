
def substr_count(n, s):
  """
  HackerRank: Special String Again.
  A string is said to be a special string if either of two conditions is met:
  - All of the characters are the same, e.g. aaa.
  - All characters except the middle one are the same, e.g. aadaa.
  A special substring is any substring of a string which meets one of those criteria. Given a string, determine how many special substrings can be formed from it.
  For example, given the string s=mnonopoo, we have the following special substrings:
  {m, n, o, n, p, o, o, non, ono, opo, oo}.
  """
  c = 0
  for i in range(0, n+1):
    for j in range(0, n-i+1):
      # All substrings
      ss = s[j:j+i]
      # Special substring
      if is_palindrome(ss) and len(set(ss)) in [1, 2]:
        c += 1
  return c

def is_palindrome(s):
  return s == s[-1::-1]