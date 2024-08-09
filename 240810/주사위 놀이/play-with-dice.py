dices = list(map(int, input().split()))
num = [0] * 6

for dice in dices:
    num[dice - 1] += 1

for i in range(6):
    print(f"{i + 1} - {num[i]}")