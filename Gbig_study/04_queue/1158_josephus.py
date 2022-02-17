from collections import deque
n, k = map(int, input().split())

q = deque(range(1, n+1))
answer = []
while len(q) != 1:
    for _ in range(k-1):
        q.append(q.popleft())
    answer.append(q.popleft())
answer.append(q[0])

print(f"<{', '.join(map(str,answer))}>")

# print("<", ", ".join(answer), ">", sep="")
# 출력부분에 있어서 앞뒤로 <> 기호를 붙여야 하기 때문에 프린트문 내부에 넣어두고,
# 그 사이에 결과 리스트를 ", "로 join하여 프린트함.
# sep="" 인자는 "<" - ", ".join(answer) - ">" 세 개를 프린트할 때 구분자를 ""로 하겠다는 의미이기 때문에 필요
# 그렇지 않으면 < 3, 6, 2, 7, 5, 1, 4 > 의 결과물이 출력됨.
#
# 1 2 3 4 5 6 7
#
# pop: 3
# 남은 큐: 4 5 6 7 1 2
#
# pop: 3, 6
# 남은 큐: 7 1 2 4 5
#
# pop: 3, 6, 2
# 남은 큐: 4 5 7 1
#
# pop: 3, 6, 2, 7
# 남은 큐: 1 4 5
#
# pop: 3, 6, 2, 7, 5
# 남은 큐: 1 4



