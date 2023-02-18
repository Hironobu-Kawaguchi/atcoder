# https://atcoder.jp/contests/arc156/tasks/arc156_a

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

def main():
    N = int(input())
    S = input()
    cnt = 0
    index_list = []
    for i, c in enumerate(S):
        if c=='1':
            cnt += 1
            index_list.append(i)
    flg = True
    if cnt%2:
        flg = False
    elif N==3 and S[1]=='1':
        flg = False

    if flg==False:
        print(-1)
    elif N==4 and cnt==2 and index_list[0]==1 and index_list[1]==2:
        print(3)
    elif cnt==2 and index_list[0]+1==index_list[1]:
        print(2)
    else:
        print(cnt//2)
    return

T = int(input())
for ti in range(T):
    main()


# S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
