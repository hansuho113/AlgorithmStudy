numbers = int(input())


for number in range(numbers):
    item_num, item_loc = map(int, input().split())
    items = list(input().split())
    items_idx = [0 for item in items]
    items_idx[item_loc] = 1
    cnt = 1

    while True:
        if items[0] == max(items):
            if items_idx[0] == 1:
                print(cnt)
                break
            items.pop(0)
            items_idx.pop(0)
            cnt += 1
        else:
            items.append(items.pop(0))
            items_idx.append(items_idx.pop(0))