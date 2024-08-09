a1, a2 = map(int, input().split())
arr = [a1, a2]

for i in range(3, 11):
    arr.append(arr[-1] + 2 * arr[-2])

for a in arr:
    print(a, end = " ")