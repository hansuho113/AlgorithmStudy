numbers = list(map(int, input().split()))
validation_num = sum([number**2 for number in numbers]) % 10
print(validation_num)