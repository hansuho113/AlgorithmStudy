from string import ascii_lowercase
from collections import Counter

data = input()
data_cnt = dict(Counter(data))

alphabets = list(ascii_lowercase)

for alphabet in alphabets:
    if alphabet in data_cnt.keys():
        print(data_cnt[alphabet])
    else:
        print(0)