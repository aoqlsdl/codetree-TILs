arr = list(map(int, input().split()))
new_arr = []

for a in arr:
    if a != 0:
        new_arr.append(a)

for n in new_arr:
    if n % 2 == 0:
        print(n // 2, end = " ")
    else:
        print(n + 3, end = " ")