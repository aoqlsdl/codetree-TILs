words = []

for i in range(10):
    word = input()
    words.append(word)

w = input()
cnt = 0

for word in words:
    if word[-1:] == w:
        print(word)
        cnt += 1

if cnt == 0:
    print("None")