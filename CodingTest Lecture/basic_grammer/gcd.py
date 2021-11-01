# a = int(input())
# b = int(input())
# n = int(1)
# a_ = []
# b_ = []
# while (n <= max(a,b)):
#     if a%n == 0:
#         a_.append(n)
#     if b%n == 0:
#         b_.append(n)
#     n += 1
# c_ = []
# for i in a_:
#     if i in b_:
#         c_.append(i)
# print(max(c_))

a, b = map(int, input().split())
n = min(a, b)
while n > 0:
    if ((a % n) == 0) & ((b % n) == 0):
        print(n)
        break
    else:
        n -= 1
