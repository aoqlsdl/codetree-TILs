word = input()

for i in range(len(word) - 1, 0, -1):
    if i % 2 == 0:
        print(word[i - 1], end = "")