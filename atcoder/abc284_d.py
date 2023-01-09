# https://atcoder.jp/contests/ABC284/tasks/abc284_d

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

def main():
    N = int(input())
    for i in range(2, int((N//2)**0.5)+1):
        if N%i==0 and (N//i)%i==0:
            p = i
            q = N//(i*i)
            break
        elif N%i==0:
            q = i
            p = int((N // i)**0.5 + 0.01)
            break
    print(p, q)
    return

T = int(input())
for ti in range(T):
    main()
