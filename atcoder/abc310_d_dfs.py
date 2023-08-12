# https://atcoder.jp/contests/abc310/tasks/abc310_d
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

N, T, M = map(int, input().split())
# print(N, T, M, file=sys.stderr)
hate = [0] * N
for i in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    hate[a] |= 1 << b
    hate[b] |= 1 << a

teams = []

def dfs(now):
    if now == N:
        return len(teams) == T
    ans = 0
    # 既にあるチームにnow番目の選手を追加する
    for i in range(len(teams)):
        if teams[i] & hate[now] == 0:
            teams[i] |= 1 << now
            ans += dfs(now + 1)
            teams[i] ^= 1 << now
    # チーム数に余裕がある時，新しいチームを作る
    if len(teams) < T:
        teams.append(1 << now)
        ans += dfs(now + 1)
        teams.pop()
    return ans

print(dfs(0))
