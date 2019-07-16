# C - Align
# https://tenka1-2018-beginner.contest.atcoder.jp/tasks/tenka1_2018_c

N = int(input())
A = [int(input()) for _ in range(N)]

A.sort()
if N % 2 == 0:
    print(-2*sum(A[:N//2-1]) - A[N//2-1] + A[N//2] + 2*sum(A[N//2+1:]))
else:
    print(-2*sum(A[:N//2-1])
          + max(-2*A[N//2-1] + A[N//2] + A[N//2+1], - A[N//2-1] - A[N//2] + 2*A[N//2+1])
          + 2*sum(A[N//2+2:]))

    # print((sum(A[N//2+1:]) - sum(A[:N//2]))*2 - min(A[N//2+1] - A[N//2], A[N//2] - A[N//2-1]))