iter_num = int(input())

for i in range(iter_num):
    str_num, string = input().split()

    tmp_list = []
    for apb in string:
        tmp_list.append(apb * int(str_num))
    print("".join(tmp_list), end="")
    tmp_list = []
