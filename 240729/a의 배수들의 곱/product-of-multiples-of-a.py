a, b = map(int, input().split())
multiple = 1

for i in range(1, b + 1):
    if (i % a == 0):
        multiple *= i

print(multiple)