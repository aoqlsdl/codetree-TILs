n, m = map(int, input().split())
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(m):
    r, c = map(int, input().split())
    arr[r - 1][c - 1] = 1

for i in range(m - 1):
    for j in range(m - 1):
        print(arr[i][j], end = " ")
    print()