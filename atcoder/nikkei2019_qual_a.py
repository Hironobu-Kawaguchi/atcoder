# https://atcoder.jp/contests/nikkei2019-qual/tasks/nikkei2019_qual_a

n, a, b = map(int, input().split())
mx = min(a, b)
mn = max(0, a+b-n)
print(mx, mn)
