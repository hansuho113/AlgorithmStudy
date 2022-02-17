# 문자열을 거꾸로 읽어서 같은지 확인
# reverse indexing 이용

### Try 1
# while True:
#     input_num = str(input())
#     if input_num == "0":
#         break
#
#     re_idx = -1  # reverse index
#     re_list = []  # reverse 01_list
#
#     for i in range(len(input_num)):
#         re_list.append(input_num[re_idx])
#         re_idx -= 1
#
#     reverse_num = "".join(re_list)
#
#     if input_num == reverse_num:
#         print("yes")
#     else:
#         print("no")


### Try 2
# input은 기본적으로 str type을 반환

while True:
    input_num = input()
    if input_num == "0":
        break
    else:
        if input_num == input_num[::-1]:
            print("yes")
        else:
            print('no')