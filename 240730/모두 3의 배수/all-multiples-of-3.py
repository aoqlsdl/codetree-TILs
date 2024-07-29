result = []
for i in range(5):
    n = int(input())
    
    if n % 3 == 0:
        result.append(n)

if len(result) == 5:
    print(1)
else:
    print(0)