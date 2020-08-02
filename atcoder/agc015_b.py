# https://atcoder.jp/contests/agc015/tasks/agc015_b

S = input()
N = len(S)

ans = N * (N-1)
for i in range(N):
    if S[i] == 'U':
        ans += i
    else:
        ans += N-1-i
print(ans)
