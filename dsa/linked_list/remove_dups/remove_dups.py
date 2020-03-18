
def remove_dups(ll_node):
  value_set = set()
  current = ll_node
  while current:
    value_set.add(current.value)
    if current.next and current.next.value in value_set:
      current.next = current.next.next
    current = current.next
  return ll_node
