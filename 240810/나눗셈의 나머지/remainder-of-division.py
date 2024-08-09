a, b = map(int, input().split())
arr = [0] * (b - 1)
hap = 0
exchange = 0

while True:
    if a <= 1:
        break
    
    a = a // b
    exchange = a % b
    arr[exchange - 1] += 1

for a in arr:
    hap += a ** 2

print(hap)