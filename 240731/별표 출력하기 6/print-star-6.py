n = int(input())

# 윗부분
for i in range(n):
    # 공백
    for j in range(i):
        print(" ", end = ' ')
    
    # * 출력
    for j in range(n + ((n - 1) - (2 * i))):
        print("*", end = ' ')
    print()

# 아랫부분
for i in range(n - 1):
    for j in range(n - 2 - i):
        print(" ", end = ' ')
    for j in range(3 + (2 * i)):
        print("*", end = ' ')
    print()