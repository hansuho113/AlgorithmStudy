word = input().upper()

apbs = list(set(word))   # set은 순서가 없는 자료형
apb_dict = {}
for i, apb in enumerate(apbs):
    apb_dict[apb] = word.count(apb)

max_cnt = max(apb_dict.values())
cnt_list = list(apb_dict.values())
if cnt_list.count(max_cnt) >= 2:
    print("?")

else:
    for key, value in apb_dict.items():
        if value == max_cnt:
            print(key)


# unq_apbs = []
# for i, apb in enumerate(apbs):
#     apb_cnt = word.count(apb)
#
#     if not unq_apbs:
#         unq_apbs.append(apb_cnt)
#         continue
#     if apb_cnt == unq_apbs[0]:   ## MMIISSS의 단어의 경우에도 s로 넘어가지 않고 ?를 출력하게 되므로 오답
#         print("?")
#         break
#     elif apb_cnt > unq_apbs[0]:
#         unq_apbs[0] = apb_cnt
#         apbs.pop(i-1)
#     elif apb_cnt < unq_apbs[0]:
#         apbs.pop(i)
#
#
# if len(apbs) < 2:
#     print(apbs[0])
