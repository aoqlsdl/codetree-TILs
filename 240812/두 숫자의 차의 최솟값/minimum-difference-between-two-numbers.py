import sys

n = int(input())
arr = list(map(int, input().split()))

min_gap = sys.maxsize

for i in range(len(arr) - 1):
    if arr[i] - arr[i + 1] > 0 and arr[i] - arr[i + 1] < min_gap:
        min_gap = arr[i] - arr[i + 1]
    elif arr[i + 1] - arr[i] > 0 and arr[i + 1] - arr[i] < min_gap:
        min_gap = arr[i + 1] - arr[i]

print(min_gap)