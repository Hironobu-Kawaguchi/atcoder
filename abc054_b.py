# https://atcoder.jp/contests/abc054/tasks/abc054_b

N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(input())

B = []
for i in range(M):
    B.append(input())

ans = 'No'

for i in range(N-M+1):
    for j in range(N-M+1):
        flg = True
        for k in range(M):
            for l in range(M):
                if A[i+k][j+l] != B[k][l]:
                    flg = False
                    break
        if flg:
            ans = 'Yes'
            break
print(ans)
