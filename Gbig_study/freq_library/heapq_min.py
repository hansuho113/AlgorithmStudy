import heapq


def heapsort(iterable):
    heap = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(heap, value)

    # 힙에 삽입된 원소를 차례대로 꺼내기
    for _ in range(len(heap)):
        result.append(heapq.heappop(heap))
    return result


result = heapsort([5, 0, 9, 4, 7, 3, 6, 1, 8, 2])
print(result)