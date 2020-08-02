# https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_a

N = int(input())
if N % 2:
    ans = N//2
else:
    ans = N//2 - 1
print(ans)
