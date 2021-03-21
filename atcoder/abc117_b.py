# B - Polygon
# https://atcoder.jp/contests/abc117/tasks/abc117_b

N = int(input())
L = list(map(int, input().split()))

mx = max(L)
els = sum(L) - mx

if mx < els:
    print('Yes')
else:
    print('No')
