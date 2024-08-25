ss = input()
ss = list(ss)

first = ss[0]
second = ss[1]

for i in range(len(ss)):
    if ss[i] == second:
        ss[i] = first

ss = ''.join(ss)
print(ss)