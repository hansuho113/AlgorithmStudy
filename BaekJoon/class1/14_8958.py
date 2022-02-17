test_size = int(input())
for test in range(test_size):
    exp = input()
    exp = exp.replace("X", ".").split(".")
    filtered_exp = list(filter(None, exp))  # None 원소 제거
    each_total = []  # filtered_exp 각 원소의 길이별 합 리스트

    for elemt in filtered_exp:
        l = len(elemt)  # 각 원소의 O 개수, for문 range의 last값으로 사용됨
        s = 0
        for i in range(1, l + 1):
            s += i
        each_total.append(s)

    print(sum(each_total))


## 문제

# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
#
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
#
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.


## 입력
#
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다.
# 문자열은 O와 X만으로 이루어져 있다.

## 출력

# 각 테스트 케이스마다 점수를 출력한다.


## 예제 입력

# - 5
# - OOXXOXXOOO
# - OOXXOOXXOO
# - OXOXOXOXOXOXOX
# - OOOOOOOOOO
# - OOOOXOOOOXOOOOX

## 예제 출력

# - 10
# - 9
# - 7
# - 55
# - 30