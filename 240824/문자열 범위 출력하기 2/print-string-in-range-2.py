word = input()
n = int(input())
length = len(word)

if n < length:
    for i in range(length - 1, length - n - 1, -1):
        print(word[i], end = "")
else:
    for i in range(length - 1, -1, -1):
        print(word[i], end = "")