import heapq


def heapsort(iterable):
    heap = []
    result = []

    for item in iterable:
        heapq.heappush(heap, -item)

    for _ in range(len(heap)):
        result.append(-heapq.heappop(heap))

    return result

result = heapsort([5, 0, 9, 4, 7, 3, 6, 1, 8, 2])
print(result)