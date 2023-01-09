# https://atcoder.jp/contests/ABC284/tasks/abc284_b

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i]%2:
            ans += 1
    print(ans)
    return

T = int(input())
for ti in range(T):
    main()
