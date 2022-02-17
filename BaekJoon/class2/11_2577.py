num_list = []
for i in range(3):
    num_list.append(int(input()))

abc = list(str(num_list[0] * num_list[1] * num_list[2]))

for i in range(10):
    print(abc.count(str(i)))
