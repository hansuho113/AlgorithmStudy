num_list = [int(input()) for i in range(9)]
max = 0
max_idx = 0

for i, num in enumerate(num_list):
    if num > max:
        max = num
        max_idx = i+1

# max값을 최소값(0)으로 설정해두고 max값보다 크면 갱신
# 01_list index 활용해서 갱신된 값의 인덱스를 max_idx로 설정

print(max)
print(max_idx)