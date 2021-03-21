# https://atcoder.jp/contests/abc087/tasks/arc090_a

N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans = max(sum(A1[:i+1]) + sum(A2[i:]), ans)

print(ans)
