# https://atcoder.jp/contests/abc153/tasks/abc153_c

N, K = map(int, input().split())
H = list(map(int, input().split()))
H.sort()
print(sum(H[:max(N-K,0)]))
