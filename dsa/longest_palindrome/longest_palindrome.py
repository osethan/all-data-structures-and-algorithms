
def longest_palindrome(s: str) -> str:
  palindrome = ''

  for i in range(1, len(s) + 1):
    for j in range(len(s)):
      substr = ''

      if j + i <= len(s):
        substr = s[j : j + i]

      if substr and is_palindrome(substr) and len(substr) > len(palindrome):
        palindrome = substr

  return palindrome


def is_palindrome(s: str) -> str:
  return s == s[-1::-1]
