dim = int(input())
directions = input().split()

# 동, 북, 서, 남 방향 벡터
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

sx, sy = 1, 1

move_types = ['R', "U", "L", "D"]
for direction in directions:
    for i in range(len(move_types)):
        if direction == move_types[i]:
            tx = sx + dx[i]
            ty = sy + dy[i]
    if (tx < 1) or (ty < 1) or (tx > dim) or(ty > dim):
        continue
    sx, sy = tx, ty

print(sx, sy)

# for direction in directions:
#     if direction == "R":
#         tx = sx + dx[0]
#         ty = sy + dy[0]
#         if (tx in range(1, dim)) and (ty in range(1, dim)):
#             sx, sy = tx, ty
#     if direction == "U":
#         tx = sx + dx[1]
#         ty = sy + dy[1]
#         if (tx in range(1, dim)) and (ty in range(1, dim)):
#             sx, sy = tx, ty
#     if direction == "L":
#         tx = sx + dx[2]
#         ty = sy + dy[2]
#         if (tx in range(1, dim)) and (ty in range(1, dim)):
#             sx, sy = tx, ty
#     if direction == "D":
#         tx = sx + dx[3]
#         ty = sy + dy[3]
#         if (tx in range(1, dim)) and (ty in range(1, dim)):
#             sx, sy = tx, ty
#
# print(str(sx) + " " + str(sy))