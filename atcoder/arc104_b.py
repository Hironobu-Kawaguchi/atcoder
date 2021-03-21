# https://atcoder.jp/contests/arc104/tasks/arc104_b
import sys
def input(): return sys.stdin.readline().rstrip()

N, S = input().split()
N = int(N)

d = {'A':0, 'T':1, 'C':2, 'G':3}
cums = [[0]*4 for _ in range(N+1)]

for i, c in enumerate(S):
    for j in range(4):
        cums[i+1][j] = cums[i][j]
    cums[i+1][d[c]] += 1

ans = 0
for l in range(N-1):
    for r in range(l+1, N):
        A = cums[r+1][0]-cums[l][0]
        T = cums[r+1][1]-cums[l][1]
        C = cums[r+1][2]-cums[l][2]
        G = cums[r+1][3]-cums[l][3]
        if (not (A^T)) and (not (C^G)):
            ans += 1
print(ans)
