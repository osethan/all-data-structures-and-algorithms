# Code Challenges

# Content
1. [Longest Palindrome](#longest-palindrome)
2. [Is Unique](#is-unique)
3. [Remove Duplicates](#remove-duplicates)

# Longest Palindrome

## Problem
Given a string `s`, find the longest palindromic substring in `s`.

## Example I/O
| In | Out |
| --- | --- |
| babad | bab |
| cbbd | bb |
| aba | aba |

## Algorithm
By brute force check all substrings one-by-one, two-by-two and all the way to the full string

1. Iterate range of substring lengths from 0 to length of string with index i
2. Iterate substrings of given length i from empty string the full string
3. If new substring is a palindrome and longer than the current longest palindrome, save the new substring
4. After step (1.), return the longest palindrome

## Pseudo Code
```python
def longest_palindrome(s: str) -> str:
  palindrome = ''

  for i in range(len(s) + 1):
    for j in range(len(s)):
      substr = ''

      if j + i <= len(s):
        substr = s[j : j + i]

      if substr and is_palindrome(substr) and len(substr) > len(palindrome):
        palindrome = substr

  return palindrome

def is_palindrome(s: str) -> str:
  return s == s[-1::-1]
```

## Complexity
| O | time | space |
| --- | --- | --- |
| longest_palindrome | O(N^2) | O(N) |
| is_palindrome | O(1) | O(1) |

*[Note No. 1]* Time taken to solve the longest palindrome problem was 1:00 hours\
*[Note No. 2]* Source of longest palindrome problem was LeetCode.com

# Is Unique

## Problem
Given a string find if the string has all unique characters.

## Example I/O
| In | Out |
| --- | --- |
| Python | True |
| Java | False |

## Algorithm
1. Lowercase string
2. Create empty set
3. For each character in string, check if character in set
4. If character in set, return False
5. Else add character to set
6. Repeat from step (3.) as needed
7. Return True

## Pseudo Code
```python
def is_unique(string: str) -> bool:
  string = string.lower()
  char_set = set()
  for char in string:
    if char in char_set:
      return False
    else:
      char_set.add(char)
  return True
```

## Complexity
| O | time | space |
| --- | --- | --- |
| is_unique | O(N) | O(N) |

*[Note No. 1]* Time taken to solve the is unique problem was 0:20 hours\
*[Note No. 2]* Source of is unique problem was Cracking the Coding Interview by Gayle Laakmann McDowell

# Remove Duplicates

## Problem
Remove all duplicates from an unsorted linked list.

## Example I/O
| In | Out |
| --- | --- |
| [2] -> [1] -> [2] -> [6] -> [6] | [2] -> [1] -> [6] |

## Algorithm
1. Make a set
2. Make current be given linked list node
3. While current exists
3. Add current.value to set
4. If current.next and current.next.value in set, make current.next be current.next.next
5. Make current be current.next
6. Repeat from step (3.) as needed
7. Return linked list

## Pseudo Code
```python
def remove_dups(ll_node):
  value_set = set()
  current = ll_node
  while current:
    value_set.add(current.value)
    if current.next and current.next.value in value_set:
      current.next = current.next.next
    current = current.next
  return ll_node
```

## Complexity
| O | time | space |
| remove_dups | O(N) | O(N) |

*[Note No. 1]* Time taken to solve the remove duplicates problem was 0:40 hours\
*[Note No. 2]* Source of longest palindrome problem was Cracking the Coding Interview by Gayle Laakmann McDowell
