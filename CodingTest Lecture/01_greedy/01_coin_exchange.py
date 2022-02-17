n = 1260
count = 0

coins = [500, 100, 50, 10]

for coin in coins:
    count += n // coin
    n %= coin

print(count)


# 동전 거스름돈 문제의 시간 복잡도는 동전의 종류가 K개라고 했을 때 O(K)이다.
# 금액과 관계없음