# https://atcoder.jp/contests/abc157/tasks/abc157_c

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

def solve():
    N, M = map(int, input().split())
    lst = [-1] * N
    for i in range(M):
        s, c = map(int, input().split())
        if s == 1 and c == 0 and N > 1:
            return -1
        elif lst[s-1] == -1:
            lst[s-1] = c
        elif lst[s-1] == c:
            continue
        else:
            return -1
    ans = ''
    for i in range(N):
        if lst[i] == -1:
            if i or N == 1:
                ans += '0'
            else:
                ans += '1'
        else:
            ans += str(lst[i])
    return ans

print(solve())
