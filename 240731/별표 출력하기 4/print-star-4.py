# n = 5이면
n = int(input())

# 첫번째 절반
for i in range(n):
    for j in range(n - i):
        print("*", end = ' ')
    print()

# 두 번째 절반
# n - 1 = 4 => i는 0, 1, 2, 3 순회 => 따라서 4줄 출력
for i in range(1, n):
    # i = 0일 때, i + 1 = 1 => j는 0 순회 => 1개 출력 => 이걸 제외하기
    # i = 1일 때, i + 1 = 2 => j는 0, 1 순회 => 2개 출력
    # i = 2일 때, i + 1 = 3 => j는 0, 1, 2 순회 => 3개 출력
    for j in range(i + 1):
        print("*", end = ' ')
    print()