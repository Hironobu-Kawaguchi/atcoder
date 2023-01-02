# https://atcoder.jp/contests/arc152/tasks/arc152_b

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)


def main():
    N, L = map(int, input().split())
    A = list(map(int, (input().split())))
    l_list, r_list = [], []
    for i in range(N):
        l_list.append(A[i])
        r_list.append(L-A[i])
    r_list.sort()
    diff = 1001001001
    l, r = 0, 0
    while True:
        diff = min(diff, abs(l_list[l]-r_list[r]))
        if l_list[l]==r_list[r]:
            break
        elif l_list[l]>r_list[r]:
            if r==N-1: break
            r += 1
        else:
            if l==N-1: break
            l += 1
    print(2*(L+diff))
    return

main()

# S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
