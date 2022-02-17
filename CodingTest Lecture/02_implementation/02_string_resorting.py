## 놓친 사항 ##
# 숫자가 하나도 포함되지 않는 경우 초기 설정한 숫자 0이 맨 뒤에 출력되지 않도록 해야 함

# strings = list(input())
#
#
# num = 0
# temp_strings = []
#
# for string in strings:
#     try:
#         num += int(string)
#     except ValueError:
#         temp_strings.append(string)
#         continue
#
# if num == 0:
#     print(''.join(sorted(temp_strings)))
# else:
#     print(''.join(sorted(temp_strings)) + str(num))

strings = list(input())
temp_strings = []
num = 0

for string in strings:
    if string.isalpha():
        temp_strings.append(string)
    else: num += int(string)
if num == 0:
    print(''.join(sorted(temp_strings)))
else:
    print(''.join(sorted(temp_strings)) + str(num))