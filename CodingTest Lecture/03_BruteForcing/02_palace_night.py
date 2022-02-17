location = input()
# row_str = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h']
# sx, sy = int(location[1]), int(row_str.index(location[0]) + 1)
#
# # UL, UR, RU, RD, DR, DL, LD ,LU
# dx = [-2, -2, -1, 1, 2, 2, 1, -1]
# dy = [-1, 1, 2, 2, 1, -1, -2, -2]

#
# count = 0
# for i in range(8):
#     tx = sx + dx[i]
#     ty = sy + dy[i]
#     if (tx < 1) or (tx > 8) or (ty < 1) or (ty >8):
#         continue
#     count += 1
# print(count)


sx = int(location[1])
sy = int(ord(location[0])) - int(ord('a')) + 1

directions = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
count = 0
for direction in directions:
    tx = sx + direction[0]
    ty = sy + direction[1]
    if (tx >= 1) and (ty >= 1) and (tx <= 8) and (ty <= 8):
        count += 1

print(count)