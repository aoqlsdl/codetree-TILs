a, b = map(int, input().split())
arr = [a, b]

for i in range(3, 11):
    if arr[-1] + arr[-2] <= 9:
        arr.append(arr[-1] + arr[-2])
    else:
        arr.append(arr[-1] + arr[-2] - 10)

for a in arr:
    print(a, end = " ")