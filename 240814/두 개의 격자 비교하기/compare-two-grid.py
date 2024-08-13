n, m = map(int, input().split())

arr_1 = [
    list(map(int, input().split()))
    for i in range(n)
]

arr_2 = [
    list(map(int, input().split()))
    for i in range(n)
]

result = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(n):
    for j in range(m):
        if arr_1[i][j] == arr_2[i][j]:
            result[i][j] = 0
        else:
            result[i][j] = 1

for arr in result:
    for elem in arr:
        print(elem, end = " ")
    print()