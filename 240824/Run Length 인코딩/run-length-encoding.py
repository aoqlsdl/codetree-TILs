A = input()
rle = ''
cnt = 1

if len(A) == 1:
    rle += A
    rle += str(cnt)
else:
    for i in range(1, len(A)):
        if A[i - 1] == A[i]:
            cnt += 1
        else:
            rle += A[i - 1]
            rle += str(cnt)
            cnt = 1
        
        if i == len(A) - 1:
            rle += A[i - 1]
            rle += str(cnt)

print(len(rle))
print(rle)