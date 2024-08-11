arr = list(map(int, input().split()))

max_val = arr[0]

for a in arr[1:]:
    if a > max_val:
        max_val = a
    else:
        continue

print(max_val)