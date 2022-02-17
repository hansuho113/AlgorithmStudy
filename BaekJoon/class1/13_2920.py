scale = "".join(input().split())

if scale == "12345678":
    print("ascending")
elif scale == "87654321":
    print('descending')
else:
    print('mixed')

#
# for i in range(0, 7):
#     curr, next = scale[i], scale[i+1]
#
#
#
# if (scale[0] == 1) and (scale[-1] == 8):
#     for i in range(1, 6):
#         if scale[i] > scale[i+1]:
#             print('mixed')
#             break
#         else:
#             continue
#     print("ascending")
#
# elif (scale[0] == 8) and (scale[-1] == 1):
#     for i in range(1, 6):
#         if scale[i] < scale[i+1]:
#             print('mixed')
#             break
#         else:
#             continue
#     print('descending')
#
# else:
#     print('mixed')
