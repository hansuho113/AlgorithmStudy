def reverser(string1):
    if len(string1) < 2:
        return string1
    reversed_words = string1.split()[::-1]
    return reversed_words


if __name__ == "__main__":
    str1 = "파이썬 알고리즘 정말 재미있다"
    print(reverser(str1))