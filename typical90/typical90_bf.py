# https://atcoder.jp/contests/typical90/tasks/typical90_bf

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

def main():
    N, K = map(int, input().split())

    def f(x):
        ret = x
        while x>0:
            ret += x % 10
            x //= 10
        return ret%100000

    vis = [-1]*100000
    vis[N] = 0
    cycle = 1
    now = f(N)
    while vis[now]==-1:
        vis[now] = cycle
        now = f(now)
        cycle += 1
        if cycle==K:
            print(now)
            return
    p1 = vis[now]
    # print(cycle, p1)
    K -= p1
    K %= cycle - p1
    # print(K)
    for k in range(K):
        # print(N)
        now = f(now)
    print(now)
    return

main()
