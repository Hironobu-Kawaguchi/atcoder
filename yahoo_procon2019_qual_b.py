# https://atcoder.jp/contests/yahoo-procon2019-qual/tasks/yahoo_procon2019_qual_b

cnt = [0] * 4
for i in range(3):
    a, b = map(int, input().split())
    cnt[a-1] += 1
    cnt[b-1] += 1
if max(cnt) >=3:
    print("NO")
else:
    print("YES")
