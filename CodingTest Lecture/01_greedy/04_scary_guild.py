n = input()
data = input()
sorted_data = map(int, sorted(data))

group = 0
count = 0

for num in sorted_data:
    group += 1
    if group >= num:
        count += 1
        group = 0

print(count)


