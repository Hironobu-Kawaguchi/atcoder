# https://atcoder.jp/contests/arc154/tasks/arc154_b

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

def main():
    N = int(input())
    S = input()
    T = input()

    if sorted(S)!=sorted(T):
        print(-1)
        return

    pos_s = N-1
    pos_t = N-1
    while pos_t>=0:
        if S[pos_s]==T[pos_t]:
            pos_s -= 1
        pos_t -= 1
    print(pos_s + 1)
    return

main()
