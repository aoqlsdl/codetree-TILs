word = input()
cnt_ee = 0
cnt_eb = 0

for i in range(len(word) - 1):
    w = word[i] + word[i + 1]

    if 'ee' == w:
        cnt_ee += 1

    if 'eb' == w:
        cnt_eb += 1

print(cnt_ee, cnt_eb)