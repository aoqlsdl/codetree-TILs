arr = list(map(int, input().split()))
new_arr = []
nums = [0] * 9

for a in arr:
    if a == 0:
        break

    new_arr.append(a)

for a in new_arr:
    num = a // 10
    if num == 0:
        continue
    else:
        nums[num - 1] += 1

for i in range(9):
    print(f"{i + 1} - {nums[i]}")