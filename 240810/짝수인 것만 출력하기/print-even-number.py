n = int(input())
arr = list(map(int, input().split()))
new_arr = [a for a in arr if a % 2 == 0]

for a in new_arr:
    print(a, end = " ")