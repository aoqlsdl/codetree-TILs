n = int(input())
nums = input().split()
result = "".join(nums)

for i in range(0, len(result), 5):
    print(result[i:i + 5:1])