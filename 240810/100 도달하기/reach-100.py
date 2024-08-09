n = int(input())
arr = [1, n]
order = 2

while True:
    arr.append(arr[order - 2] + arr[order - 1])

    if arr[order - 2] + arr[order - 1] > 100:
        break
    else:
        order += 1

for a in arr:
    print(a, end = " ")