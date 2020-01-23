# https://atcoder.jp/contests/yahoo-procon2019-qual/tasks/yahoo_procon2019_qual_c

K, A, B = map(int, input().split())
if B-A > 2:
    tmp = max((K-A+1)//2, 0)    # Bの回数
    ans = 1 + tmp * (B-A) + (K-tmp*2)
else:
    ans = 1 + K
print(ans)
