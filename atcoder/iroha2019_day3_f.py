# F - 闇のカードゲーム
# https://atcoder.jp/contests/iroha2019-day3/tasks/iroha2019_day3_f
# N = 2k+1 として、すぬけ君はk枚、いろはちゃんは(k-1)枚カードを取り、残り2枚の差を最大化する
# a[i+k+1] - a[i]を最大化する

N = int(input())
a = list(map(int, input().split()))
k = N // 2

ans = a[-1]
for i in range(N-k-1):
    ans = min(a[i+k+1] - a[i], ans)
print(ans)
