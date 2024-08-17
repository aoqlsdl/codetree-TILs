n, m = map(int, input().split())

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

result = 1
summary = 0

while summary <= n * m:
    for i in range(n):
        for j in range(m):
            if i + j == summary:
                arr[i][j] = result
                result += 1
            elif i + j != summary:
                continue
    summary += 1
        
for i in range(n):
    for j in range(m):
        print(arr[i][j], end = " ")
    print()

# i + j의 합이 같을 때 result += 1
# arr[0][0] = 1  arr[0][1] = 2  arr[0][2] = 4
# arr[1][0] = 3  arr[1][1] = 5  arr[1][2] = 7
# arr[2][0] = 6  arr[2][1] = 8  arr[2][2] = 9