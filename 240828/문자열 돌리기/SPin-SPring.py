s = input()
L = len(s)

for i in range(L + 1):
    print(s)
    s = s[-1] + s[:-1]