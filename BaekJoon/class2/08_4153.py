import sys

while True:
    num_list = list(map(int, sys.stdin.readline().split()))
    if sum(num_list) == 0:
        break
    max_line = num_list.pop(num_list.index(max(num_list)))
    if max_line**2 == (num_list[0]**2) + (num_list[1]**2):
        print("right")
    else:
        print("wrong")

##### 코드 길이 개선 #####
# 처음에 짠 코드에서는 입력받은 리스트에서 맥스값을 pop했는데 이 방법 외에
# 리스트 자체를 정렬해두고 리스트 인덱스로 접근하면 코드 길이 개선 가능
