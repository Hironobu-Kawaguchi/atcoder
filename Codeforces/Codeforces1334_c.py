# https://codeforces.com/contest/1334/problem/C

import sys
# def input(): return sys.stdin.readline().rstrip()
# input = sys.stdin.readline
input = sys.stdin.buffer.readline
INF = 1001002003004005006

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        ans, mi, blast = 0, INF, 0
        for i in range(n):
            a, b = map(int, input().split())
            if i:
                if a > blast:
                    ans += a - blast
                    mi = min(mi, blast)
                else:
                    mi = min(mi, a)
            else:
                a0 = a
            blast = b
        ans += max(0, a0 - blast)
        mi = min(mi, min(a0, blast))
        print(ans + mi)

    return

main()
