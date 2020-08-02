# https://atcoder.jp/contests/abc134/tasks/abc134_c

N = int(input())

M1, M2 = 0, 0
A = []
for i in range(N):
    a = int(input())
    A.append(a)
    if a > M1:
        M2 = M1
        M1 = a
    elif a > M2:
        M2 = a

for i in range(N):
    if A[i] == M1:
        print(M2)
    else:
        print(M1)
