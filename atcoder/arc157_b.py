# https://atcoder.jp/contests/arc157/tasks/arc157_b
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

d = {'X':0, 'Y':1}
def main():
    N, K = map(int, input().split())
    S = input()
    cntx = 0
    for i in range(N):
        if S[i]=='X':
            cntx += 1
    lst = []
    if K<=cntx:
        for i in range(N):
            lst.append(d[S[i]])
    else:
        K = N - K
        for i in range(N):
            lst.append(1 - d[S[i]])
    # print(K, lst)
    cnt_list = []
    cnt = 0
    for i in range(N):
        if lst[i]==0:
            cnt += 1
        else:
            if cnt>0:
                if i-cnt==0:
                    cnt_list.append((1, cnt, i-cnt))
                else:
                    cnt_list.append((0, cnt, i-cnt))
                cnt = 0
    else:
        if cnt>0:
            cnt_list.append((1, cnt, N-cnt))
    cnt_list.sort()
    # print(cnt_list)
    for flg, num, idx in cnt_list:
        if K==0: break
        if idx==0:
            for i in range(idx+num-1, idx-1, -1):
                lst[i] += 1
                K -= 1
                if K==0: break
        else:
            for i in range(idx, idx+num):
                lst[i] += 1
                K -= 1
                if K==0: break
    # print(lst)
    ans = 0
    for i in range(N-1):
        if lst[i]==lst[i+1]==1:
            ans += 1
    print(ans)
    return

main()
