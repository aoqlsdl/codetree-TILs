s = input()

for i in range(len(s) - 1):
    n = int(input())
    if n >= len(s):
        s = s[:len(s) - 1]
    else:
        s = s[:n] + '' +s[n + 1:]
    print(s)