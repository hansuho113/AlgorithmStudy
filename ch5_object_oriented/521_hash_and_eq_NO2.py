class Symbol(object):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.value == other.value
        else:
            return NotImplemented


if __name__ == '__main__':
    x = Symbol("Py")
    y = Symbol("Py")

    symbols = set()
    symbols.add(x)
    symbols.add(y)

    print(x is y)
    print(x == y)
    print(len(symbols))


# eq 메서드를 재정의하면 Symbol 클래스 unhashable 에러 발생
# 이는 가변 객체임을 의미하는데 set은 불변 객체이다. 이를 고치기 위해 __hash__메서드를 추가