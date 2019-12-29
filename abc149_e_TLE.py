# https://atcoder.jp/contests/abc149/tasks/abc149_e

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

AA = []
for i in range(N):
    for j in range(N):
        AA.append(A[i]+A[j])
AA.sort(reverse=True)

ans = 0
for i in range(M):
    ans += AA[i]

print(ans)


# TLE解法
# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# A.sort(reverse=True)

# AA = []
# for i in range(N):
#     for j in range(N):
#         AA.append(A[i]+A[j])
# AA.sort(reverse=True)

# ans = 0
# for i in range(M):
#     ans += AA[i]

# print(ans)
