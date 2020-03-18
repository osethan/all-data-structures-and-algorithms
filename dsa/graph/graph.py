
class Graph:
  """
  Graph as adjacency list data structure.
  """

  def __init__(self):
    """
    Graph constructor.
    """

    self.vertices = []


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
