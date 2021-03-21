# B - AtCoder Market
# https://atcoder.jp/contests/s8pc-6/tasks/s8pc_6_b

N = int(input())
A, B = [], []
for i in range(N):
    ab = list(map(int, input().split()))
    A.append(ab[0])
    B.append(ab[1])
AB = A + B
AB.sort()

ans = 10 ** 10
for left in range(len(AB)):
    for right in range(left, len(AB)):
        tmp = 0
        for i in range(N):
            tmp += abs(AB[left] - A[i]) + (B[i] - A[i]) + abs(AB[right] - B[i])
        ans = min(tmp, ans)
print(ans)
