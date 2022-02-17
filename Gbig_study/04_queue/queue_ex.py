from collections import deque

collections_queue = deque([1,2,3])
collections_queue.append(4)
print(collections_queue)

collections_queue.popleft()
collections_queue.popleft()
print(collections_queue)

collections_queue.pop()
print(collections_queue)

collections_queue.appendleft(1)
collections_queue.append(4)
print(collections_queue)

# deque의 popleft()와 appendleft(x) 메서드는 모두 O(1)의 시간 복잡도를 가지기짐
# 하지만 내부적으로는 Linked list를 사용하고 있기 때문에 N번째 데이터에 접근하려면 N번의 순회가 필요
# 따라서, 데이터 접근에 대한 시간복잡도는 기본적으로 O(N)임
