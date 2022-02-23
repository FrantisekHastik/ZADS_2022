import math

def dijkstra_search(graph_matrix, start_node, dest_node):
    
    node_count = len(graph_matrix)
    visited = [False] * node_count
    distance = [math.inf] * node_count
    distance[start_node] = 0
    current_node = start_node
    neighbours = []

    while not visited[dest_node]:
        neighbours = graph_matrix[current_node]
        for node in range(node_count):
            if (not visited[node]) and (neighbours[node] is not None):
                path = distance[current_node] + neighbours[node]
                if path < distance[node]:
                    distance[node] = path
        visited[current_node] = True
        min_distance = math.inf
        for new_node in range(node_count):
            if (not visited[new_node]) and (distance[new_node] < min_distance):
                min_distance = distance[new_node]
                current_node = new_node
        if min_distance == math.inf:
            break
    return distance[dest_node]

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
