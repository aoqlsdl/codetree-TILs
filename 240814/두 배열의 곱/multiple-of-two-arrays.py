arr_1 = [
    list(map(int, input().split()))
    for i in range(3)
]
blank = input()
arr_2 = [
    list(map(int, input().split()))
    for i in range(3)
]

for i in range(3):
    multi = 1
    for j in range(3):
        multi = arr_1[i][j] * arr_2[i][j]
        print(multi, end = " ")
    print()