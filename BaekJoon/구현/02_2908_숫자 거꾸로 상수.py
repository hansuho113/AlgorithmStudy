num1, num2 = map(lambda x: int(x[::-1]), input().split())

if num1 < num2:
    print(num2)
else:
    print(num1)