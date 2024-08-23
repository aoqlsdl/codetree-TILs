A = input()
rle = ''
cnt = 1

for i in range(len(A) - 1):
    if A[i] == A[i + 1]:
        cnt += 1
    else:
        rle += A[i]
        rle += str(cnt)
        cnt = 1
    
    if i == len(A) - 2:
        rle += A[i]
        rle += str(cnt)

print(len(rle))
print(rle)