import sys
num = int(sys.stdin.readline())

for n in range(num):
    infos = list(map(int, sys.stdin.readline().split()))
    H, W, N = infos[0]+1, infos[1]+1, infos[2]-1

    room_list = []
    for floor in range(1, H):
        for room in range(1, W):
            room_list.append((floor, str(room).zfill(2)))

    room_list.sort(key=lambda room: (room[1], room[0]))

    print(str(room_list[N][0]) + room_list[N][1])