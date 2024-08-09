a, b = map(int, input().split())
arr = [0] * b
hap = 0
exchange = 0

while True:
    if a <= 1:
        break
    
    exchange = a % b
    a = a // b
    arr[exchange] += 1

for a in arr:
    hap += a ** 2

print(hap)