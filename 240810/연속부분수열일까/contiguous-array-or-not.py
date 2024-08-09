n1, n2 = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

is_sequnce = False

for i in range(len(A)):
    new_A = A[i:len(B) + i]
    if new_A == B:
        is_sequnce = True
        break
    else:
        is_sequnce = False

if is_sequnce:
    print("Yes")
else:
    print("No")