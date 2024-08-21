import sys

word_1 = input()
word_2 = input()
word_3 = input()

max_length = 0
min_length = 0

if (len(word_1) > len(word_2) and len(word_1) > len(word_3)):
    max_length = len(word_1)
elif (len(word_2) > len(word_1) and len(word_2) > len(word_3)):
    max_length = len(word_2)
else:
    max_length = len(word_3)

if (len(word_1) < len(word_2) and len(word_1) < len(word_3)):
    min_length = len(word_1)
elif (len(word_2) < len(word_1) and len(word_2) < len(word_3)):
    min_length = len(word_2)
else:
    min_length = len(word_3)

print(max_length - min_length)