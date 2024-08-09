n = int(input())
counting = [0] * 9
arr = list(map(int, input().split()))

for a in arr:
    counting[a - 1] += 1

for c in counting:
    print(c)