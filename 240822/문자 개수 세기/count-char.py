str1 = input()
alpha = input()

cnt = 0

for s in str1:
    if s == alpha:
        cnt += 1

print(cnt)