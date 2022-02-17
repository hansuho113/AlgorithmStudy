n, m = map(int, input().split())

min_value = 0
for i in range(n):
    temp_min = min(list(map(int, input().split())))
    if temp_min > min_value:
        min_value = temp_min

print(min_value)



