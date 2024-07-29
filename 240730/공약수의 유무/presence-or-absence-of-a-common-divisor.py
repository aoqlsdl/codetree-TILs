a, b = map(int, input().split())
result = []

for i in range(a, b + 1):
    if (1920 % i == 0) and (2880 % i == 0):
        result.append(i)
    else:
        continue

if len(result) != 0 :
    print(1)
else:
    print(0)