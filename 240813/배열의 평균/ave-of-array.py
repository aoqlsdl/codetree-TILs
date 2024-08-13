arr = [
    list(map(int, input().split()))
    for i in range(2)
]

hap = 0

for i in range(2):
    hap_column = 0

    for j in range(4):
        hap_column += arr[i][j]
        hap += arr[i][j]
    
    print("{:.1f}".format(hap_column / 4), end = " ")

print()

for i in range(4):
    hap_row = 0
    for j in range(2):
        hap_row += arr[j][i]
    print("{:.1f}".format(hap_row / 2), end = " ")

print()
print("{:.1f}".format(hap / 8), end = " ")