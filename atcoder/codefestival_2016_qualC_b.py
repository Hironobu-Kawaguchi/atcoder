# https://atcoder.jp/contests/code-festival-2016-qualc/tasks/codefestival_2016_qualC_b

K, T = map(int, input().split())
a = list(map(int, input().split()))
mxa = max(a)
ans = max(mxa-1-(K-mxa), 0)
print(ans)
