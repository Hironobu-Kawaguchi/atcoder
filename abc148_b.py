# https://atcoder.jp/contests/abc148/tasks/abc148_b

N = int(input())
S, T = input().split()

ans = ''
for i in range(N):
    ans += S[i]
    ans += T[i]
print(ans)
