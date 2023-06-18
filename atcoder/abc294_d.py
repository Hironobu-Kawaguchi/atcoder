# https://atcoder.jp/contests/abc294/tasks/abc294_d

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
import bisect

def main():
    N, Q = map(int, input().split())
    min_uncall = 0
    min_call = 0
    gone = [False]*N
    for iq in range(Q):
        event = list(map(int, (input().split())))
        if event[0]==1:
            min_uncall += 1
        elif event[0]==2:
            x = event[1]
            gone[x-1] = True
            if min_call==x-1:
                for i in range(x, N):
                    if gone[i]==False:
                        min_call = i
                        break
        else:
            print(min_call + 1)
        # print(iq, event, min_uncall, min_call, gone)
    return

main()


    # S = input()
    # N = int(input())
    # N, K = map(int, input().split())
    # A = list(map(int, (input().split())))
    # A = [[int(i) for i in input().split()] for _ in range(N)]
