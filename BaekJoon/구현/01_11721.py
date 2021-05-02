s = input()
s_len = len(list(s)) + 1

if s_len < 10:    # 문자열 길이 10 미만이면 그대로 출력
    print(s)

else:
    full_line = s_len // 10
    part_line = s_len % 10

    for i in range(full_line):
        print(s[i*10:(i*10+10)])    # 십의 자리수 만큼 반복하면서 10자리씩 출력

    if part_line != 0:
        print(s[(full_line)*10:(full_line+part_line)])    # 남은 일의 자리가 0이 아니라면 십의 자리 반복한 것 이후부터 출력

