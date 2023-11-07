# https://atcoder.jp/contests/abc327/tasks/abc327_a

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
S = input()
for i in range(N-1):
    if S[i:i+2] == 'ab' or S[i:i+2] == 'ba':
        print('Yes')
        exit()
print('No')
