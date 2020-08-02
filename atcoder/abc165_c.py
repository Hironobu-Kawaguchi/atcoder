# https://atcoder.jp/contests/abc165/tasks/abc165_c
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

from itertools import combinations_with_replacement

def main():
    N, M, Q = map(int, input().split())
    a,b,c,d = [],[],[],[]
    for i in range(Q):
        _a,_b,_c,_d = map(int, input().split())
        a.append(_a-1)
        b.append(_b-1)
        c.append(_c)
        d.append(_d)
    ans = 0
    for A in combinations_with_replacement(range(M), N):
        # print(A)
        tmp = 0
        for i in range(Q):
            if A[b[i]] - A[a[i]] == c[i]:
                tmp += d[i]
        ans = max(ans, tmp)
    print(ans)
    return
main()

# X = int(input())
# S = input()
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
