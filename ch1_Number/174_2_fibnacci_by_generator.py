def fib_gen():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b


if __name__ == "__main__":
    fg = fib_gen()
    for _ in range(10):
        print(next(fg), end=" ")