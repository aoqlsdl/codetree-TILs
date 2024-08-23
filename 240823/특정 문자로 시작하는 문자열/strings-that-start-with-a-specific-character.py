n = int(input())
words = []

for i in range(n):
    word = input()
    words.append(word)

w = input()

cnt = 0
length = 0

for word in words:
    if word[0] == w:
        cnt += 1
        length += len(word)

print(cnt, "{:.2f}".format(length / cnt))