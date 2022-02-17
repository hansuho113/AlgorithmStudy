import random

def testing_random():
    """ random 모듈 테스트 """
    values = [1,2,3,4]
    print(random.choice(values))
    print(random.choice(values))
    print(random.choice(values))
    print(random.sample(values, 2))
    print(random.sample(values, 3))

    """ shuffle the value list """
    random.shuffle(values)
    print(values)

    """ generate the any number in 0 to 10 """
    print(random.randint(1, 10))
    print(random.randint(1, 10))

if __name__ == "__main__":
    testing_random()