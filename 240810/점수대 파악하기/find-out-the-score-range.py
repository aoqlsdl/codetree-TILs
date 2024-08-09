grades = list(map(int, input().split()))
new_grades = []
arr = [0] * 10

for grade in grades:
    if grade == 0:
        break

    new_grades.append(grade)

for grade in new_grades:
    n = grade // 10
    if n == 0:
        continue
    else:
        arr[n - 1] += 1

for i in range(10, 0, -1):
    print(f"{i * 10} - {arr[i - 1]}")