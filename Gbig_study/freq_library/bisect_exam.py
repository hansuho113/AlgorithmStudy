from bisect import bisect_left, bisect_right


b = [1, 3, 5, 7, 7, 9]
x = 5

def count_by_range(count_list, l_value, r_value):
    r_index = bisect_right(count_list, r_value)
    l_index = bisect_left(count_list, l_value)

    return r_index - l_index


count_list = [-1, 0, 0, 2, 4, 4, 4, 6, 6, 8]

print(count_by_range(count_list, 4, 4))
print(count_by_range(count_list, -1, 4))