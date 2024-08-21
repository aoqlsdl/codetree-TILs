s = input()
arr = ["apple", "banana", "grape", "blueberry", "orange"]
new_arr = []

for a in arr:
    for i in range(2,4):
        if s in a[i]:
            new_arr.append(a)

for a in new_arr:
    print(a)

print(len(new_arr))