n = int(input())
nums = list(map(int, input().split()))
appear = 0
idx = 0

for num in nums:
    if num == 2:
        appear += 1
    idx += 1    
    if appear == 3:
        print(idx)
        break