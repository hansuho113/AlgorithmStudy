import string
alphabet_list = list(string.ascii_lowercase)

s = input()
for alpha in alphabet_list:
    print(s.count(alpha), end=" ")
