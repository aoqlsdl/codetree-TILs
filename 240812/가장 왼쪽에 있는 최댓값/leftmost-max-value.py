import sys 

n = int(input())
arr = list(map(int, input().split()))
max_val = -sys.maxsize

while True:
    if len(arr) == 1:
        print(1)
        break
    elif len(arr) == 0:
        break
    
    for i in range(len(arr)):
        if arr[i] >= max_val:
            max_val = arr[i]

    print(arr.index(max_val) + 1, end = " ")

    arr = arr[:arr.index(max_val)]
    max_val = 0