from collections import Counter


def counter_ex():
    """ 항목의 발생 횟수를 매핑하는 딕셔너리를 생성한다."""
    seq1 = [1, 2, 3, 5, 1, 2, 5, 5, 2, 5, 1, 4]
    seq_cnts = Counter(seq1)
    print(seq_cnts)

    """수동 갱신 혹은 update() 메서드 사용도 가능"""
    seq2 = [1, 2, 3]
    seq_cnts.update(seq2)
    print(seq_cnts)

    seq3 = [1, 4, 3]
    for key in seq3:
        seq_cnts[key] += 1
    print(seq_cnts)

    """a+b, a-b 같은 셋 연산을 사용할 수도 있음"""
    seq_cnts_2 = Counter(seq3)
    print(seq_cnts_2)
    print(seq_cnts + seq_cnts_2)
    print(seq_cnts - seq_cnts_2)


if __name__ == '__main__':
    counter_ex()