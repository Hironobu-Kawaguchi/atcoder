"""
B - Digital Gifts
https://atcoder.jp/contests/abc119/tasks/abc119_b
高橋くんは N 人の親戚からお年玉をもらいました。
N 個の値 x1,x2,...,xN と N 個の文字列 u1,u2,...,uN が入力されます。各文字列 ui は JPY または BTC であり、xi と ui が i 人目の親戚からのお年玉の内容を表します。
例えば、x1= 10000, u1= JPY であれば 1 人目の親戚からのお年玉は 10000 円であり、x2= 0.10000000, u2= BTC であれば 2 人目の親戚からのお年玉は 0.1 ビットコインです。
ビットコインを 1.0 BTC あたり 380000.0 円として換算すると、高橋くんがもらったお年玉は合計で何円に相当するでしょうか？
"""
"""
N = int(input())
rate = 380000.0
ans = 0.0
for i in range(N):
    x, u = input().split()
    x = float(x)
    ans += x * rate if u == 'BTC' else x
print('{:.11f}'.format(ans))
"""
N = int(input())
ans = 0.0
for _ in range(N):
    x, u = input().split()
    if u == 'JPY':
        ans += float(x)
    elif u == 'BTC':
        ans += float(x) * 380000.0
print(ans)