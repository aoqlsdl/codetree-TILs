s, q = input().split()
q = int(q)

for i in range(q):
    s = list(s)
    n, a, b = input().split()
    n = int(n)

    if n == 1:
        a = int(a)
        b = int(b)

        ath = s[a - 1]
        bth = s[b - 1]
        
        s[a - 1] = bth
        s[b - 1] = ath
        # print(s[a-1], s[b-1])

    elif n == 2:
        for j in range(len(s)):
            if s[j] == a:
                s[j] = b
        
    s = ''.join(s)
    print(s)