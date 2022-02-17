def recursive(i):
    # 종료 조건 꼭 필요
    if i == 100:
        return
    print(f"{i}번째 재귀함수에서 {i+1}번째 재귀함수 호출")
    recursive(i+1)
    print(f"{i}번째 재귀함수 종료")

recursive(90)

# 재귀함수는 스택 구조로 동작함
# 차례로 재귀함수를 호출해서 메모리에 쌓은 뒤 마지막에 쌓인 재귀함수부터 처리하면서 종료함
