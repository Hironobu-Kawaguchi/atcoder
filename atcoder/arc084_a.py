# https://atcoder.jp/contests/abc077/tasks/arc084_a

import bisect
N = int(input())
A = list(map(int, input().split()))
A.sort()
B = list(map(int, input().split()))
C = list(map(int, input().split()))
C.sort()

ans = 0
for i in range(N):
    cnta = bisect.bisect_left(A, B[i])
    cntc = bisect.bisect_right(C, B[i])
    ans += cnta * (N - cntc)

print(ans)
