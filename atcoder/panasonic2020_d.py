# https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_d

import sys
# # input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

from string import ascii_lowercase
# print(ascii_lowercase)
d = dict(zip(ascii_lowercase, range(26)))
# print(d['a'])
N = int(input())

def nexts(s, n, maxnum):
    if n == N:
        print(s)
        return
    for i in range(maxnum+1):
        nexts(s + ascii_lowercase[i], n+1, max(maxnum,i+1))

nexts('a', 1, 1)
