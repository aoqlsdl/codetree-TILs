A = input()
B = input()
lenA = len(A)
lenB = len(B)
while True:
    idx = -1

    candidates = lenA - lenB +1
    for i in range(candidates):
        is_same = True
        for j in range(lenB):
            if  A[i+j] != B[j]:
                is_same = False
                break
        if is_same:
            idx = i
    if  idx == -1:
        break
    A= A[:idx]+A[idx+lenB:]
    lenA = len(A)
print(A)