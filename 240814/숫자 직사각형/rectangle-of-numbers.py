n, m = map(int, input().split())

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

num = 1
for i in range(n):
    for j in range(m):
        arr[i][j] = num
        print(arr[i][j], end = " ")
        num += 1
    print()