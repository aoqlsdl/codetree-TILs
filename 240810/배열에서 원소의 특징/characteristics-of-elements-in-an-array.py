arr = list(map(int, input().split()))
n = 0

for a in arr:
    if a % 3 == 0:
        break
    
    n += 1

print(arr[n - 1])