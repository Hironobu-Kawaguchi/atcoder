# https://atcoder.jp/contests/abc136/tasks/abc136_d

S = input()
N = len(S)

ans = [0] * N

r, l = 0, 0
for i in range(N):
    if S[i] == 'R' and l != 0:
        ans[i-l-1] = r//2 + r % 2 + l//2
        ans[i-l]   =  r//2 + l//2 + l % 2
        r, l = 1, 0
    elif S[i] == 'R':
        r += 1
    elif S[i] == 'L':
        l += 1
ans[N-l-1] = r//2 + r % 2 + l//2
ans[N-l]   =  r//2 + l//2 + l % 2

print(*ans)
