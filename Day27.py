from collections import deque

def shortest_path(V, edges, start, end):
    graph = [[] for _ in range(V)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  

    queue = deque()
    queue.append((start, 0))  
    
    visited = [False] * V
    visited[start] = True
    
    while queue:
        node, dist = queue.popleft()
        
        if node == end:
            return dist
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, dist + 1))
    
    return -1


V = 5
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]
start, end = 0, 4

print(shortest_path(V, edges, start, end))  
