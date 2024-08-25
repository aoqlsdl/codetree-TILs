A = input()
B = input()

cnt = 0

for i in range(len(A) - 1):
    w = A[i] + A[i + 1]

    if w == B:
        cnt += 1

print(cnt)