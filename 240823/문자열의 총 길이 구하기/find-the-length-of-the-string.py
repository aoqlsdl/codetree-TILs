words = input().split()
cnt = 0

for word in words:
    for w in word:
        cnt += 1

print(cnt)