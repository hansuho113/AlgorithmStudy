from collections import deque

n = int(input())
q = deque(range(1, n+1))

while len(q) > 2:
    q.popleft()
    q.append(q.popleft())
print(q[-1])

# 시작과 동시에 제일 위에 있는 카드를 버리므로 n-1까지의 큐를 생성하고 시작
## 하려고 했으나 input이 3인 경우에 [1,2]의 큐를 가지고 시작하면 while문에서 오류 발생해서 안 됨

# 하나의 숫자만 받을 때는 굳이 sys를 쓸 필요가 없는 건가
# list나 queue 생성 시용 리스트컴프리헨션 말고 range 활용
# 이전에 풀이는 while문을 1보다 클 동안 실행시켰던 것을 2까지 하고 2개 중 뒷 요소를 프린트하는 것으로 바꿈
