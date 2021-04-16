import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()

m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

def binary_search(num, num_list):
    first, last = 0, len(num_list)
    while True:
        if first == last:
            print(0)
            return
        mid = (first + last) // 2
        if num_list[mid] == num:
            print(1)
            return
        elif num < num_list[mid]:
            first, last = first, mid
        elif num > num_list[mid]:
            first, last = mid+1, last
        else:
            print(0)
            return





# def binary_search(num, num_list, first, last):
#     if (len(num_list) == 0) | (num > num_list[-1]):  # list가 없거나 찾는 수가 (정렬된)리스트에 없을 경우
#         print(0)
#         return
#     mid = (first + last) // 2
#
#     if num_list[mid] == num:
#         print(1)
#         return
#     elif num < num_list[mid]:
#         binary_search(num, num_list[:mid], first, mid-1)  # 데이터를 줄여줘야함
#     elif num > num_list[mid]:
#         binary_search(num, num_list[mid:], mid, last)
#     else:
#         print(0)
#         return


for m_num in m_list:
    # first, last = 0, len(n_list)
    binary_search(m_num, n_list)

# import sys
#
# n = int(sys.stdin.readline())
# n_list = list(map(int, sys.stdin.readline().split()))
#
# m = int(sys.stdin.readline())
# m_list = list(map(int, sys.stdin.readline().split()))
#
# for m_num in m_list:
#     if m_num in n_list:
#         print(1)
#     else:
#         print(0)