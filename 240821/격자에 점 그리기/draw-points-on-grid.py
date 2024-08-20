n, m = map(int, input().split())
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]
dot = 1

for i in range(m):
    r, c = map(int, input().split())
    arr[r - 1][c - 1] = dot
    dot += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = " ")
    print()