
def is_unique(string):
  """
  Find if a string has all unique characters.

  In:
  string (str): String to check for unique characters.

  Out:
  (boolean): Whether the string has all unique characters.
  """

  string = string.lower()
  char_set = set()
  
  for char in string:
    if char in char_set:
      return False
    else:
      char_set.add(char)
  
  return True
