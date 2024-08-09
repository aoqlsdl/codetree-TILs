n = int(input())
multi = 1
arr = []
multi_5 = 0

while True:
    elem = n * multi
    
    if elem % 5 == 0:
        multi_5 += 1

    arr.append(elem)
    multi += 1
    
    if multi_5 == 2:
        break


for a in arr:
    print(a, end = " ")