num = int(input())
from collections import deque
cards = deque(range(1, num+1))

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])





### 시간초과
# cards = [i for i in range(1, num+1)]
#
# while True:
#     if len(cards) != 1:
#         cards.pop(0)
#         cards.append(cards.pop(0))
#     else:
#         print(cards[0])
#         break
