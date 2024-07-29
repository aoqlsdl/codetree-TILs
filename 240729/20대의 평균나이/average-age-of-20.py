summary = 0
cnt = 0

while True:
    age = int(input())

    if age >= 20 and age <= 29:
        summary += age
        cnt += 1
        True
    else:
        break

result = summary / cnt
print(f"{result:.2f}")