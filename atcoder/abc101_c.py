# https://atcoder.jp/contests/abc101/tasks/abc101_c

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = -(-(N-1) // (K-1))

print(ans)
