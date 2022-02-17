import random
from typing import Sequence, Any

def find_max(a: Sequence) -> Any:
    maximum = a[0]

    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]

    return maximum


if __name__ == '__main__':
    print("난수의 최대값 구하기")

    num = int(input("난수의 개수를 입력하시오: "))
    min_value = int(input("난수 범위의 최소값을 입력하시오: "))
    max_value = int(input("난수 범위의 최대값을 입력하시오: "))

    random_list = [None] * num
    for i in range(num):
        random_list[i] = random.randint(min_value, max_value)

    print(random_list)
    print(f"랜덤 리스트 중 최대값은 {find_max(random_list)} 입니다.")
