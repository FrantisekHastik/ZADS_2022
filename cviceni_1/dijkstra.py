import math

def dijkstra_search(graph_matrix, start_node, dest_node):
    #Insert code here
    return 42

graph = [[0, 5, 3, 4, None, None],
         [5, 0, 1, None, 3, None],
         [3, 1, 0, 1, 10, None],
         [4, None, 1, 0, 6, None],
         [None, 3, 10, 6, 0, None],
         [None, None, None, None, None, None]]
print("Test 1 expects: 3")
print("Test 1 gets:    " + str(dijkstra_search(graph, 0, 2)))
print("Test 2 expects: 5")
print("Test 2 gets:    " + str(dijkstra_search(graph, 3, 4)))
print("Test 3 expects: 7")
print("Test 3 gets:    " + str(dijkstra_search(graph, 0, 4)))
print("Test 4 expects: inf")
print("Test 4 gets:    " + str(dijkstra_search(graph, 0, 5)))
