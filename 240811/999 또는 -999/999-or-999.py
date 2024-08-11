import sys

arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 999 or arr[i] == -999:
        min_val = sys.maxsize
        max_val = -sys.maxsize
        for a in arr[:i]:
            if min_val > a:
                min_val = a
            elif max_val < a:
                max_val = a

print(f"{max_val} {min_val}")