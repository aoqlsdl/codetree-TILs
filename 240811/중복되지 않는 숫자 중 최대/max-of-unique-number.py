import sys

n = int(input())
arr = list(map(int, input().split()))
max_val = -1

for a in arr:
    if a > max_val and arr.count(a) == 1:
        max_val = a

print(max_val)