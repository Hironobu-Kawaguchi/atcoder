# https://atcoder.jp/contests/abc021/tasks/abc021_b

N = int(input())
a, b = map(int, input().split())
K = int(input())
P = list(map(int, input().split()))

s = set(P)
if a in s or b in s or len(s) != K:
    print("NO")
else:
    print("YES")
    