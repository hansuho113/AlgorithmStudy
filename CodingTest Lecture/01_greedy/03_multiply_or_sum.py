# import time
#
# num_list = list(map(int, input()))
#
#
# if num_list[0] and num_list[1] == 0 or 1:
#     start_num = num_list[0] + num_list[1]
# else: start_num = num_list[0] * num_list[1]
#
#
# for num in num_list[2:]:
#     if num == (0 or 1):
#         start_num += num
#     else:
#         start_num *= num
#
# print(start_num)
# e = time.time()


data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if (num <= 1) or (result <= 1):
        result += num
    else:
        result *= num

print(result)
