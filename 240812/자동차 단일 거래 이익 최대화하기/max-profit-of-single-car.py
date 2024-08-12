import sys

n = int(input())
prices = list(map(int, input().split()))

price = sys.maxsize
max_profit = 0

for p in prices:
    if price > p:
        price = p
    
    if (p - price > 0) and (p - price> max_profit):
        max_profit = p - price

print(max_profit)