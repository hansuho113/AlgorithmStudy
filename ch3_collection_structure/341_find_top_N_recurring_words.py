from collections import Counter


def find_top_N_recurring_words(seq, N):
    """
    :param seq: 문자열
    :param N: top N (최빈 단어 상위 N개)
    :return : 문자열에서 단어 등장 빈도 순으로 반환(동일한 개수이면 앞 단어부터 등장)
    """
    dcnt = Counter()
    for word in seq.split():
        dcnt[word] += 1
    return dcnt.most_common(N)


def test_find_top_N_recurring_words():
    seq = "안 녕 하 세 요 안 녕 안 녕 해 요"
    N = 3
    N2 = 5
    assert(find_top_N_recurring_words(seq, N) == [('안', 3), ('녕', 3), ('요', 2)])
    assert(find_top_N_recurring_words(seq, N2) == [('안', 3), ('녕', 3), ('요', 2), ('하', 1), ('세', 1)])
    print("테스트 통과")


if __name__ == '__main__':
    test_find_top_N_recurring_words()