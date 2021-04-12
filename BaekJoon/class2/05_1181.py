import sys

n = int(sys.stdin.readline())

# 문자를 입력받고 중복된 문자를 제거 한 후 리스트에 삽입
sentence = list(set([sys.stdin.readline().strip() for i in range(n)]))

words = [(len(word), word) for word in sentence]    # 튜플이 원소인 리스트 생성
words.sort(key=lambda word: (word[0], word[1]))    # 단어 길이, 단어 순으로 오름차순 정렬

for word in words:
    print(word[1])