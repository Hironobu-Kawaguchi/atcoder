# 蟻本をPythonで (初級編)
# https://qiita.com/saba/items/affc94740aff117d2ca9
# 2-2 猪突猛進！ "貪欲法"
# 例題 2-2-2　区間スケジューリング問題

# 多次元リストの sort に使える
from operator import itemgetter

n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

st = sorted([(s[i], t[i]) for i in range(n)], key=itemgetter(1))

ans = 0
# 最後に選んだ仕事の終了時間
last = 0

for i in range(n):
    if last < st[i][0]:
        ans += 1
        last = st[i][1]

print(ans)