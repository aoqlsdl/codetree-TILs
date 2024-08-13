arr = [
    list(map(str, input().split()))
    for i in range(5)
]

for i in range(5):
    for j in range(3):
        print(arr[i][j].upper(), end = " ")
    print()