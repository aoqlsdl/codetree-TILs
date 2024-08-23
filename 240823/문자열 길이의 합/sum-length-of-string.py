n = int(input())
words = []

for i in range(n):
    word = input()
    words.append(word)

cnt_all = 0
cnt_a = 0

for word in words:
    if word[0] == 'a':
        cnt_a += 1
    
    for w in word:
        cnt_all += 1

print(cnt_all, cnt_a)