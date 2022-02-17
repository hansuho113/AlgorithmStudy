import math


def fib_seq_iter(n):
    if n < 2: return n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def fib_seq_rec(n):
    if n < 2: return n
    return fib_seq_rec(n - 1) + fib_seq_rec(n - 2)


def fib_seq_form(n):
    sq5 = math.sqrt(5)
    phi = (1 + sq5) / 2
    return int(math.floor(phi ** n / sq5))


def test_fib():
    n = 10
    assert (fib_seq_rec(n) == 55)
    assert (fib_seq_iter(n) == 55)
    assert (fib_seq_form(n) == 55)
    print("테스트 통과")


if __name__ == "__main__":
    test_fib()
