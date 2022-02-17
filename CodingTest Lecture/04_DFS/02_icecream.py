N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))
# 문자열의 경우 split해서 list로 만들 필요 없이 바로 list로 캐스팅하면 문자열 개별로 이루어진 list로 분리, 저장됨


def check_ice(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        check_ice(x-1, y)   # 상
        check_ice(x+1, y)   # 하
        check_ice(x, y-1)   # 좌
        check_ice(x, y+1)   # 우
        return True
    return False

ice_count = 0
for n in range(N):
    for m in range(M):
        if check_ice(n, m):
            ice_count += 1

print(ice_count)
