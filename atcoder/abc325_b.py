# https://atcoder.jp/contests/abc325/tasks/abc325_b

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
W, X = [], []
for _ in range(N):
    w, x = map(int, input().split())
    W.append(w)
    X.append(x)
ans = 0
for i in range(24):
    tmp = 0
    for j in range(N):
        if 9<=(i+X[j])%24<18:
            tmp += W[j]
    ans = max(ans, tmp)
print(ans)
