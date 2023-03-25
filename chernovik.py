def ford_fulkerson(graph, source, sink):
    """
    Implementation of the Ford-Fulkerson algorithm to find the maximum flow in a network.
    :param graph: A dictionary representing the graph in adjacency list format.
    :param source: The source node in the graph.
    :param sink: The sink node in the graph.
    :return: The maximum flow in the network.
    """
    # Initialize the residual graph
    residual_graph = {}
    for node in graph:
        residual_graph[node] = {}
        for neighbor in graph[node]:
            residual_graph[node][neighbor] = graph[node][neighbor]

    # Initialize the flow to 0
    max_flow = 0

    # Loop until there is no more augmenting path
    while True:
        # Find an augmenting path using BFS
        parent = {}
        visited = set()
        queue = [source]
        visited.add(source)
        while queue:
            node = queue.pop(0)
            for neighbor in residual_graph[node]:
                if neighbor not in visited and residual_graph[node][neighbor] > 0:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    queue.append(neighbor)
        if sink in visited:
            # Find the bottleneck capacity
            bottleneck_capacity = float('inf')
            node = sink
            while node != source:
                bottleneck_capacity = min(bottleneck_capacity, residual_graph[parent[node]][node])
                node = parent[node]
            # Update the flow and residual graph
            node = sink
            while node != source:
                residual_graph[parent[node]][node] -= bottleneck_capacity
                if (node, parent[node]) in residual_graph:
                    residual_graph[node][parent[node]] += bottleneck_capacity
                else:
                    residual_graph[node][parent[node]] = bottleneck_capacity
                node = parent[node]
            max_flow += bottleneck_capacity
        else:
            break

    return max_flow
graph = {
    'a': {'b': 4, 'c': 3, 'd':4},
    'b': {'a': 0, 'c': 2, 'f': 3},
    'c': {'a': 0, 'b': 2, 'd': 3, 'e': 1, 'f': 2},
    'd': {'a': 0, 'c': 3, 'e':2, 'g':5},
    'e': {'c': 1, 'd':2, 'g':2},
    'f': {'b': 3, 'c': 2, 'g':3},
    'g': {'d':0, 'e':0, 'f':0}
}

source = 'a'
sink = 'g'

print(ford_fulkerson(graph, source, sink))