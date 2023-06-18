# https://atcoder.jp/contests/abc296/tasks/abc296_a

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

def main() -> None:
    N: int = int(input())
    S: str = input().rstrip()
    for i in range(N-1):
        if S[i]==S[i+1]:
            print("No")
            return
    print("Yes")
    return

main()
