# https://atcoder.jp/contests/typical90/tasks/typical90_ah

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
A = list(map(int, (input().split())))
for i in range(N): A[i] -= 1

ans = 0
l = 0
r = 0
cnt = {A[0]: 1}

while r<N-1:
    if len(cnt)<K:
        r += 1
        if A[r] in cnt:
            cnt[A[r]] += 1
        else:
            cnt[A[r]] = 1
    elif len(cnt)==K:
        if A[r+1] in cnt:
            r += 1
            cnt[A[r]] += 1
        else:
            if cnt[A[l]]==1:
                cnt.pop(A[l])
            else:
                cnt[A[l]] -= 1
            l += 1
    # print(ans, l, r, r-l+1, len(cnt), cnt)
    ans = max(ans, r-l+1)

print(ans)
