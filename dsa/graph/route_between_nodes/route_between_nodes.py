from dsa.graph.graph import Graph, GraphVertex
from dsa.stacks_and_queues.stacks_and_queues import Queue


def route_between_nodes(g, s, e):
  """
  Find if there's a path from node s to node e in graph g.

  In:
  g (Graph): Graph being searched.
  s (GraphVertex): Starting node.
  e (GraphVertex): Search node.

  Out:
  (boolean): Whether there's a path from node s to node e in graph g.
  """

  seen = set()
  queue = Queue()
  queue.add(s)

  while not queue.is_empty():
    node = queue.remove()
    if str(node) == str(e):
      return True
    if str(node) in seen:
      continue
    seen.add(str(node))
    for neighbor in node.neighbors:
      queue.add(neighbor)
  
  return False
