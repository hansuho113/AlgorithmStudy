# 깊이 우선 탐색
# 그래프를 파이썬의 2차원 리스트로 표현 가능
#   2차원 리스트의 각 원소의 인덱스를 실제 그래프의 노드 번호와 동일하게 맞추고
#   이후 해당 인덱스 원소에 속하는 1차원 리스트에 인덱스 번호와 연결된 노드들을 표현

# 그래프의 노드 번호가 1부터 시작하므로 0번째 인덱스에 해당하는 부분은 빈 리스트로 하고 사용하지 않음
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

# 방문 여부를 나타내는 리스트; 이것도 graph와 마찬가지로 실제 노드 번호와 맞추기 위해 9개까지 사용
visited = [False] * 9

def dfs(graph, v, visited):
    visited[v] = True   # 방문한 v번 노드는 True로 방문 처리
    print(v, end=' ')
    # 현재 노드와 연결된 노드들을 재귀적으로 방문; graph의 v번 노드에 해당하는 1차원 원소에 속하는 리스트 (graph[v])
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)

# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]
#
# visited = [False] * 9
#
#
# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end=' ')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
#
#
# dfs(graph, 1, visited)