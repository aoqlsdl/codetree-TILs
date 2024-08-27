A = input()
B = input()

while B in A:
    idx = A.find(B)
    A = A[:idx] + A[idx + 2:]
print(A)

# while True:
# for i in range(len(A)):
#     print(f"i: {i}, i + 2: {i + 2}")
#     print(f"i: {A[i:i + 2]}")
#     if A[i:i + 2] == B:
#         A = list(A)
#         A.pop(i)
#         A.pop(i + 1)
#         A = ''.join(A)
#     else:
#         print("False")

# print(A)


# # A = ''.join(A)
# # print(A)