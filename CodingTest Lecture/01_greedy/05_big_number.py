cnt, m, k = map(int, input().split())

num_list = list(map(int, input().split()))

first_num = num_list.pop(num_list.index(max(num_list)))
second_num = max(num_list)

answer = first_num * (k * (m // k)) + second_num * (m % k)
print(answer)


# 가장 큰 수와 다음으로 큰 수를 first_num, second_num 에 저장
# first_num을 (m을 k로 나눈 몫) * k 번 곱합
# second_num을 (m을 k로 나눈 나머지 번 곱함