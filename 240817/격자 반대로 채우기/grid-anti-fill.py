n = int(input())
cnt = 1

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n - 1, -1, -1):
    if (n - i) % 2 == 0:
        for j in range(n):
            arr[j][i] = cnt
            cnt += 1
    else:
        for j in range(n - 1, -1, -1):
            arr[j][i] = cnt
            cnt += 1
    
for i in range(n):
    for j in range(n):
        print(arr[i][j], end = " ")
    print()