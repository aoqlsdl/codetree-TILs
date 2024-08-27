a = input()
cmd = input()

for c in cmd:

    if c == "L":
        a = a[1:] + a[0]
    else:
        a = a[-1] + a[:-1]

print(a)