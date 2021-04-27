num = int(input())
first_num = num

cnt = 0
while True:
    if num == 0:
        print(1)
        break

    tenth = num // 10    # 십의 자리
    oneth = num % 10    # 일의 자리
    if num < 10:
        tenth = 0
        oneth = num

    sum_num = tenth + oneth    # 십의 자리 + 일의 자리
    sum_oneth = sum_num % 10

    new_num = (oneth * 10) + sum_oneth

    cnt += 1
    if new_num == first_num:
        print(cnt)
        break
    num = new_num
