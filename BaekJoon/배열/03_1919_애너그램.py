# 애너그램은 단순히 대칭되는 문자열을 뜻하는 것이 아니라, 순서를 바꾸어서 같아질 수 있는 두 단어를 뜻함
# 문자를 순서하는 위치는 상관없음

## 문제를 잘 읽어보아야 함


a_str = list(input())
b_str = list(input())
result = 0

for i in range(ord('a'), ord('z')+1):
    result += abs(a_str.count(chr(i)) - b_str.count(chr(i)))

print(result)

