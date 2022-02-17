import sys
# vps: Valid Paranthesis String
num = int(sys.stdin.readline())

for _ in range(num):
    target = list(sys.stdin.readline().strip())
    temp = []    # 입력 괄호 문자열 확인용 빈 스택
    # "(" 이면 스택에 추가
    # 스택이 비어있지 않을 때 ")" 이면 스택 pop, 스택이 비어있을 때면 break, not vps
    for x in target:
        if x == "(":
            temp.append(x)
        else:
            if len(temp) == 0:
                temp.append(x)
                break
            else: temp.pop()

    if len(temp) == 0:
        print("YES")
    else: print("NO")


# sys.stdin.readline() 개행문자 처리
# input = sys.stdin.readline()
# a = list(input)
# print(f"a-> {a}")
#
# b = input.strip()
# print(f"b-> {b}")
#
# c = input.strip('\n')
# print(f"c-> {c}")