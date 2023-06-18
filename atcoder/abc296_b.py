# https://atcoder.jp/contests/abc296/tasks/abc296_b

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

def main():
    S = [input().rstrip() for _ in range(8)]
    for i in range(8):
        for j in range(8):
            if S[i][j] == '*':
                ans = chr(ord('a') + j) + str(8 - i)
                print(ans)
                return
    return

main()
