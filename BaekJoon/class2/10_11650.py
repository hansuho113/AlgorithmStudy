import sys

num = int(sys.stdin.readline())

coord_list = []
for n in range(num):
    inputs = list(map(int, sys.stdin.readline().split()))
    coord_list.append((inputs[0], inputs[1]))

coord_list.sort()

for coord in coord_list:
    print(coord[0], coord[1])