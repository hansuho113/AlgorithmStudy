def finding_gcd(a, b):
    while(b != 0):
        result = b
        a, b = b, a % b   # a에 b를 대입, b에 a를 b로 나눈 나머지 대입
    return result

# 유클리드 호제법
#  1. x % y = 0 이라면 gcd(x, y) = y가 성립
#  2. x % y !=0 이라면 gcd(x, y) = gcd(x, x%y)가 성립
#  1번이 될 때까지 1-2번을 반복

def test_finding_gcd():
    n1 = 21
    n2 = 12
    assert(finding_gcd(n1, n2) == 3)
    print(finding_gcd(n1, n2))
    print("테스트 통과")

if __name__ == "__main__" :
    test_finding_gcd()