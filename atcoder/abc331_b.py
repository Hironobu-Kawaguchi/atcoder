# https://atcoder.jp/contests/abc331/tasks/abc331_b

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

INF = 10 ** 18
N, S, M, L = map(int, input().split())

ans = INF

for s in range((N+6-1)//6+1):
    for m in range((N+8-1)//8+1):
        for l in range((N+12-1)//12+1):
            if 6*s+8*m+12*l >= N:
                ans = min(ans, S*s+M*m+L*l)
print(ans)

