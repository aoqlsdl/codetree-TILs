n = int(input())
arr = list(map(int, input().split()))

new_arr = [a * a for a in arr]

for a in new_arr:
    print(a, end = " ")