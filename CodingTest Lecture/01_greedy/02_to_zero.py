# greedy 알고리즘은 아이디어를 찾아내고, 이것이 정당성을 갖는지 여부를 생각해봐야

import time
N, K = map(int, input().split())
count = 0
s = time.time()
while True:
    target = (N//K)*K
    count += (N-target)
    N = target
    if N<K: break
    count += 1
    N //=K

count+=(N-1)
print(count)
e = time.time()
print(e-s)



#
#
#
#
#
# s = time.time()
# def func1(num):
#     return num-1
#
#
# def func2(num):
#     return num // K
#
#
# while True:
#     if N % K == 0:
#         N = func2(N)
#     else:
#         N = func1(N)
#     count += 1
#     if N == 1:
#         break
#
# print(count)
# e = time.time()
#
# print(e-s)
