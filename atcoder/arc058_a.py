# https://atcoder.jp/contests/abc042/tasks/arc058_a

N, K = map(int, input().split())
D = list(input().split())

ans = N
flg = True
while flg:
    s = str(ans)
    for c in s:
        if c in D:
            ans += 1
            break
    else:
        flg = False
print(ans)
