from typing import Any, Sequence


def find_max(a: Sequence) -> Any:
    maximum = a[0]

    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]

    return maximum


if __name__ == '__main__':
    print("배열의 최대값 구하기")

    num = int(input('원소의 개수: '))
    x = [None] * num   # num만큼의 길이를 가진 None 배열 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하시오.'))
    print(f"최대값은 {find_max(x)}입니다")

