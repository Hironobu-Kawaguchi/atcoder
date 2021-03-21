# https://atcoder.jp/contests/abc078/tasks/arc085_a

N, M = map(int, input().split())

time = 1900 * M + 100 *(N-M)
rounds = 2 ** M
ans = time * rounds
print(ans)