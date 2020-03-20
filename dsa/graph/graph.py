
class Graph:
  """
  Graph as adjacency list data structure.
  """

  def __init__(self):
    """
    Graph constructor.
    """

    self.vertices = []


  def add(self, value):
    """
    Add vertex to graph with value.

    In:
    value (): Any data to be the value of the new vertex.
    """

    vertex = GraphVertex(value)
    self.vertices += [vertex]
    return vertex


  def add_edge(self, s, e):
    """
    Add edge from start vertex to end vertex.

    In:
    s (GraphVertex): Start vertex.
    e (GraphVertex): End vertex.
    """

    s.neighbors += [e]


class GraphVertex:
  """
  Vertex in a graph data structure.  
  """

  def __init__(self, value):
    """
    Vertex constructor.
    """

    self.value = value
    self.neighbors = []


  def __repr__(self):
    """
    String representation of vertex.
    """

    return str(self.value)
