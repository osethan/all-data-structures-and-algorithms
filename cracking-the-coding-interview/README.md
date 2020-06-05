# Cracking the Coding Interview


# Content

## Chapeter 1. Arrays and Strings

1. [Is Unique](#is-unique)

## Chapter 2. Linked Lists

1. [Remove Dups](#remove-dups)


# Is Unique

## Time
| Given | Taken | Notes |
| --- | --- | --- |
| 1:00 hours | 0:20 hours | Alternative solution found |

## Problem
Given a string find if the string has all unique characters. What if no other data structures can be used?

## Examples
In: Python, Out: True\
In: Java, Out: False

## Questions
Q1: Do uppercase characters count as different characters?\
A: No

Q2: What can I return for an empty string?\
A: True

Q3: Can I assume punctuation should be unique too?\
A: Yes

## Algorithm
1. Lowercase string
2. Create empty set
3. For each character in string, check if character in set
4. If character in set, return False
5. Else add character to set
6. Repeat from step (3.) as needed
7. Return True

## Code
```python
def is_unique(string):
  string = string.lower()
  char_set = set()
  for char in string:
    if char in char_set:
      return False
    else:
      char_set.add(char)
  return True
```

## Tests
I would make test cases checking the cases I clarified before starting to solve the problem

## Big O
| O | is_unique |
| --- | --- |
| time | O(N) |
| space | O(N) |

## *Alternative Solution*
If I couldn't use additional data structures I would check each character against the others in a nested loop

## Algorithm
1. Lowercase string
2. For each character in string, compare against all characters at different index
3. If characters match, return False
4. Repeat from step (2.) as needed
5. Return True

## Code
```python
def is_unique(string):
  string = string.lower()
  for i, char in enumerate(string):
    for j, target in enumerate(string):
      if i != j and char == target:
        return False
  return True
```

## Tests
Tests stay the same as the first solution

## Big O
| O | is_unique |
| --- | --- |
| time | O(N^2) |
| space | O(1) |x


# Remove Dups

## Time
| Given | Taken | Notes |
| --- | --- | --- |
| 1:00 hours | 0:40 hours | Alternative solution not found |

## Problem
Remove all duplicates from an unsorted linked list. How could the problem be solved without a temporary buffer?

## Examples
In: [2] -> [1] -> [2] -> [3] -> [6]\
Out: [2] -> [1] -> [3] -> [6]

## Questions
Q1: Which duplicate value should be kept?\
A: The first

Q2: Given an empty linked list can I return an empty linked list?\
A: Yes

Q3: Should I modify the linked list in place or make a new linked list?\
A: Modify in place

Q4: Is the linked list a doubly linked list?\
A: No

Q5: Is the linked list circular?\
A: No

## Algorithm
1. Make set
2. Make current = linked_list.head
3. While current
4. Add current.value to set
5. If current.next and current.next.value in set, make current.next = current.next.next
6. Make current = current.next
7. Repeat from step (3.) as needed
8. Return linked list

## Code
```python
def remove_dups(ll):
  value_set = set()
  current = ll.head
  while current:
    value_set.add(current.value)
    if current.next and current.next.value in value_set:
      current.next = current.next.next
  return ll
```

## Tests
Test cases for questions asked as edge cases at the start of solving the problem

## Big O
| O | remove_dups |
| --- | --- |
| time | O(N) |
| space | O(N) |
