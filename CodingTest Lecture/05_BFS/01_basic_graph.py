# BFS: Breadth-First Search
# 간선의 비용이 모두 같은 경우의 최단 경로를 구할 때 사용

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    # 큐가 빌 때까지
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)
