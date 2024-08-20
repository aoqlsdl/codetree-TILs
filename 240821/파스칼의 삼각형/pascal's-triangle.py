n = int(input())
arr = [
    [0 for _ in range(i + 1)]
    for i in range(n)
]


if n > 1:
    for i in range(2):
        for j in range(len(arr[i])):
            arr[i][j] = 1
            
    for i in range(2, n):
        for j in range(len(arr[i])):
            if j == 0 or j == len(arr[i]) - 1:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
    for i in range(n):
        for j in range(len(arr[i])):
            print(arr[i][j], end = " ")
        print()
else:
    print(1)