
def longest_palindrome_substr(s):
  """
  Given a str find the longest palindrome substr
  """
  pal = ''
  for i in range(1, len(s)+1):
    for j in range(len(s)-i+1):
      ss = s[j:j+i]
      if is_palindrome(ss) and len(ss) > len(pal):
        pal = ss
  return pal

def is_palindrome(s):
  return s == s[-1::-1]