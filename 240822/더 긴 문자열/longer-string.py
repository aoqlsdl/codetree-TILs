word_1, word_2 = map(str, input().split())

if len(word_1) > len(word_2):
    print(word_1, len(word_1))
elif len(word_1) < len(word_2):
    print(word_2, len(word_2))
else:
    print("same")