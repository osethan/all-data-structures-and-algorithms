# Code Challenges

# Content
1. [Longest Palindrome](#longest-palindrome)
2. [Is Unique](#is-unique)
3. [Remove Duplicates](#remove-duplicates)
4. [Stack Min](#stack-min)
5. [Route Between Nodes](#route-between-nodes)
6. [Minimal Tree](#minimal-tree)

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
| --- | --- | --- |
| remove_dups | O(N) | O(N) |

*[Note No. 1]* Time taken to solve the remove duplicates problem was 0:40 hours\
*[Note No. 2]* Source of remove duplicates problem was Cracking the Coding Interview by Gayle Laakmann McDowell

# Stack Min

## Problem
How would you design a stack which has a min function? Functions push, pop and min should all have runtime O(1).

## Algorithm
For every value added to the stack, add another value to a different stack which shows the min at each level of the stack.

## Example I/O
```
[5] [1]
[1] [1]
[2] [2]
[6] [4]
[4] [4]
```

## Pseudo Code
```python
class MinStack(Stack):
  def __init__(self):
    super().__init__()
    self.min_stack = Stack()

  def push(self, value):
    super().push(value)
    if self.min_stack.is_empty():
      self.min_stack.push(value)
    else:
      min_val = self.min_stack.peek()
      if value < min_val:
        self.min_stack.push(value)
      else:
        self.min_stack.push(min_val)

  def pop(self):
    value = super().pop()
    self.min_stack.pop()
    return value

  def min(self):
    return self.min_stack.peek()
```

*[Note No. 1]* Time taken to solve the stack min problem was 0:30 hours\
*[Note No. 2]* Source of stack min problem was Cracking the Coding Interview by Gayle Laakmann McDowell

# Route Between Nodes

## Problem
Given a directed graph and two nodes S and E, design an algorithm which finds if there's a path from S to E.

## Example I/O
```
In:
[S] -> [A] <- [B]
|
v
[C] -> [D] -> [E]

Out: True
```

## Algorithm
Breadth First Search

1. Add node S to queue
2. While queue isn't empty
3. Remove front of queue
4. If removed front is E, return True
5. If removed front in set, continue
6. Add removed front to set
7. Add removed front's neighbors to queue
8. After step (2.), return False

## Pseudo Code
```python
def route_between_nodes(g, s, e):
  seen = set()
  queue = Queue()
  queue.add(s)

  while not queue.is_empty():
    node = queue.remove()
    if node == e:
      return True
    if node in seen:
      continue
    seen.add(node)
    for neighbor in node.neighbors:
      queue.add(neighbor)
  
  return False
```

## Complexity
| O | time | space |
| --- | --- | --- |
| route_between_nodes | O(V + E) | O(V) |

## Tests
1. S and E not connected, no other paths
2. S and E not connected, other paths
3. S and E directly connected
4. S and E indirectly connected

*[Note No. 1]* Time taken to solve the route between nodes problem was 0:25 hours\
*[Note No. 2]* Source of route between nodes problem was Cracking the Coding Interview by Gayle Laakmann McDowell

# Minimal Tree

## Problem
Given a sorted list of unique integers, write a function which creates a BST with minimum height.

## Example I/O
```
In: [1, 2, 3, 4, 5, 6, 7]

Out:
        [4]
      /     \
    [2]      [6]
  /   \      /  \
[1]   [3]  [5]  [7]
```

## Algorithm
Apply binary search on the sorted list used to make the BST.

1. Find mid of list, make node with value at mid index
2. Node left is return of recursive call of [0:mid] sublist. If sublist[0] == sublist[mid], no left
3. Node right is return of recursive call of [mid+1:] sublist. If sublist[-1] == sublist[mid], no right
4. Return node from step (1.)

## Pseudo Code
```python
def minimal_tree(lst):
  if len(lst) == 0:
    return None

  mid = len(lst) // 2
  node = TreeNode(mid)

  left = None
  if lst[0] == lst[mid]:
    left = minimal_tree([])
  else:
    left = minimal_tree(lst[0:mid])

  right = None
  if lst[-1] == lst[mid]:
    right = minimal_tree([])
  else:
    right = minimal_tree(lst[mid+1:])

  node.left = left
  node.right = right
  return node
```

## Complexity
| O | time | space |
| --- | --- | --- |
| minimal_tree | O(N) | O(N) |

## Tests
1. 3 value list, mid has left and right values
2. 2 value list, mid has left but no right values
3. 1 value list, mid has no left and no right values
4. 5 value list, many level BST

*[Note No. 1]* Time taken to solve the minimal tree problem was 0:35 hours\
*[Note No. 2]* Source of minimal tree problem was Cracking the Coding Interview by Gayle Laakmann McDowell
