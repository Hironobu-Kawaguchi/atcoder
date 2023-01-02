# https://atcoder.jp/contests/arc109/tasks/arc109_c
# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
import copy

N, K = map(int, input().split())
S = input()
d = {'R': 0, 'P': 1, 'S':2}

def win(x, y):
    tmp = (d[y]-d[x]+3)%3
    if tmp==1: return y
    else: return x

lst = list(S)

for i in range(K):
    t = copy.copy(lst) + copy.copy(lst)
    for j in range(N):
        lst[j] = win(t[j*2], t[j*2+1])
    # print(i, lst)

print(lst[0])
