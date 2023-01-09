# https://atcoder.jp/contests/ABC204/tasks/abc204_e
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

import heapq


def main():
    N, M = map(int, input().split())
    to = [[] for _ in range(N)]
    for i in range(M):
        a, b, c, d = map(int, input().split())
        to[a-1].append((b-1, c, d))
        to[b-1].append((a-1, c, d))
    # print(to)

    done = [False] * N

    def dfs(now, done):
        if done[now]==True: return
        done[now] = True
        for next, _, _ in to[now]:
            dfs(next, done)
        return

    dfs(0, done)
    if done[N-1]==False:
        print(-1)
        return

    done = [False] * N
    done[0] = True
    now = 0
    q = []
    for next, c, d in to[now]:
            t = max(0, int(d**0.5 + 0.5)-1)
            # while d > (t+1)*(t+2): t += 1
            heapq.heappush(q, (t + c + d//(t+1), next))

    while len(q):
        t0, now = heapq.heappop(q)
        if done[now]: continue
        done[now] = True
        if now == N-1:
            print(t0)
            return
        for next, c, d in to[now]:
                t = max(t0, int(d**0.5 + 0.5)-1)
                # while d > (t+1)*(t+2): t += 1
                heapq.heappush(q, (t + c + d//(t+1), next))

main()
