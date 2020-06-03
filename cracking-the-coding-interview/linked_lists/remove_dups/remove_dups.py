
def remove_dups(ll):
  """
  Remove duplicate values from a linked list.

  In:
  ll (LinkedList): Linked list to remove duplicates from.

  Out:
  (LinkedList): Same linked list modified in place.
  """

  value_set = set()
  current = ll.head

  while current:
    value_set.add(current.value)
    if current.next and current.next.value in value_set:
      current.next = current.next.next
    current = current.next

  return ll
