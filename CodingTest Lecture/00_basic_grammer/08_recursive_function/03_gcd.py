# Greatest Common Devider

# A, B 두 수가 있을 때 A를 B로 나눈 나머지를 R이라고 하자. (단, A > B)
# 이 때 A-B의 최대공약수는 B-R의 최대공약수와 같다.

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(gcd(192, 162))