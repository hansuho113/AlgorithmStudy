## Iterator
# 이터레이터는 이터레이터 프로토콜을 구형하는 컨테이너 객체라고 할 수 있음
# - 컨테이너의 다음 값을 반환하는 __next__() 메서드와 이터레이터 자신을 반환하는 __iter__() 메서드를 기반으로 함
#
# 제너레이터는 최종값을 반환하지만, 이터레이터는 yield 키워드를 사용하여 코드 실행 중에 값을 반환한다.
# - 즉, __next__() 메서드를 호출할 때마다 어떤 값 하나를 추출한 후 해당 yield 표현식의 값을 반환한다.
# - StopIteration 예외가 발생할 때까지 값을 반환함

a = [1,2,3,4]
def f(a):
    while a:
        yield a.pop()

x = f(a)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))