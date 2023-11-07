# https://atcoder.jp/contests/abc322/tasks/abc322_a

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
S = input()
cc = "ABC"
for i in range(N-2):
    if S[i:i+3] == cc:
        print(i+1)
        exit()
else:
    print(-1)
    