import sys 

n = int(input())
arr = list(map(int, input().split()))

min_val = sys.maxsize
cnt = 0

for a in arr:
    if min_val > a:
        min_val = a
        cnt = 1
    elif min_val == a:
        cnt += 1

print(f"{min_val} {cnt}")