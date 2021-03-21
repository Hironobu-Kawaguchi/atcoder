# https://atcoder.jp/contests/abc033/tasks/abc033_b

N = int(input())
S, P = [], []
for i in range(N):
    s, p = input().split()
    S.append(s)
    P.append(int(p))
sump = sum(P)
ans = "atcoder"
for i in range(N):
    if P[i] * 2 > sump:
        ans = S[i]
        break
print(ans)
