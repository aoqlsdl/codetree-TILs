arr = ['L', 'E', 'B', 'R', 'O', 'S']
s = str(input())
idx = -1

for i in range(6):
    if arr[i] == s:
        idx = i

if idx == -1:
    print("None")
else:
    print(idx)