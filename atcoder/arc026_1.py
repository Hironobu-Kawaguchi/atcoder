# https://atcoder.jp/contests/arc026/tasks/arc026_1

N, A, B = map(int, input().split())
nb = min(5, N)
ans = (N-nb)*A + nb*B
print(ans)
