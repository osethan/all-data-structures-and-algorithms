import pytest

from dsa.graph.graph import Graph
from dsa.graph.route_between_nodes.route_between_nodes import route_between_nodes


def test_route_between_nodes_two_nodes_no_edges():
  """
  For a graph with two nodes and no edges, no path exists.
  """

  graph = Graph()
  s = graph.add('s')
  e = graph.add('e')

  expected = False
  actual = route_between_nodes(graph, s, e)
  assert actual == expected


def test_route_between_nodes_path_no_connection():
  """
  For a graph with start node and end node islands, no path exists.
  """

  graph = Graph()
  s = graph.add('s')
  a = graph.add('a')
  b = graph.add('b')
  e = graph.add('e')
  
  graph.add_edge(s, a)
  graph.add_edge(a, b)

  expected = False
  actual = route_between_nodes(graph, s, e)
  assert actual == expected


def test_route_between_nodes_nonlinear_path_no_connection():
  """
  For a graph with start node and end node complex islands, no path exists.
  """

  graph = Graph()
  s = graph.add('s')
  a = graph.add('a')
  b = graph.add('b')
  c = graph.add('c')
  e = graph.add('e')
  
  graph.add_edge(s, a)
  graph.add_edge(s, b)

  graph.add_edge(b, c)

  expected = False
  actual = route_between_nodes(graph, s, e)
  assert actual == expected


def test_route_between_nodes_two_nodes_connected():
  """
  For a graph with start node and end node directly connected, a path exists.
  """

  graph = Graph()
  s = graph.add('s')
  e = graph.add('e')
  graph.add_edge(s, e)

  expected = True
  actual = route_between_nodes(graph, s, e)
  assert actual == expected


def test_route_between_nodes_linear_connection():
  """
  For a graph with start node and end node connected through neighbors, a path exists.
  """

  graph = Graph()
  s = graph.add('s')
  a = graph.add('a')
  e = graph.add('e')

  graph.add_edge(s, a)
  graph.add_edge(s, e)

  expected = True
  actual = route_between_nodes(graph, s, e)
  assert actual == expected


def test_route_between_nodes_nonlinear_connection():
  """
  For a graph with start node and end node nonlinearly connected through neighbors, a path exists.
  """
  
  graph = Graph()
  s = graph.add('s')
  a = graph.add('a')
  b = graph.add('b')
  e = graph.add('e')

  graph.add_edge(s, a)
  graph.add_edge(s, b)

  graph.add_edge(b, e)

  expected = True
  actual = route_between_nodes(graph, s, e)
  assert actual == expected
