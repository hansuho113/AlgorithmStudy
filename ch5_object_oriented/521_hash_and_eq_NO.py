class Symbol(object):
    def __init__(self, value):
        self.value = value


if __name__ == '__main__':
    x = Symbol("Py")
    y = Symbol("Py")

    symbols = set()
    symbols.add(x)
    symbols.add(y)

    print(x is y)
    print(x == y)
    print(len(symbols))


# 파이썬 사용자 정의 클래스의 모든 객체는 hashable한데,
# 이는 hash() 속성을 호출할 수 있다는 뜻이며 불변객체임을 나타냄