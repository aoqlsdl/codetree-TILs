import sys

word_1 = input()
word_2 = input()
word_3 = input()

len1 = len(str1)
len2 = len(str2)
len3 = len(str3)

mx = max([len1, len2, len3])
mn = min([len1, len2, len3])

print(mx - mn)