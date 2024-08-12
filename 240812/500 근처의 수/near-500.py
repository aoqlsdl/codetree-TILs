import sys

arr = list(map(int, input().split()))

min_val_500 = sys.maxsize
max_val_500 = -sys.maxsize

for a in arr:
    if a < 500 and a > max_val_500:
        max_val_500 = a
    elif a > 500 and a < min_val_500:
        min_val_500 = a

print(max_val_500, min_val_500)