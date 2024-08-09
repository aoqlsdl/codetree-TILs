n, q = map(int, input().split())
elem = list(map(int, input().split()))

for i in range(q):
    ask = list(map(int, input().split()))
    
    if ask[0] == 1:
        print(elem[ask[1] - 1])
    elif ask[0] == 2:
        if ask[1] in elem:
            print(elem.index(ask[i]) + 1)
        else:
            print(0)
    elif ask[0] == 3:
        for i in range(ask[1], ask[2] + 1):
            print(elem[i - 1], end = " ")