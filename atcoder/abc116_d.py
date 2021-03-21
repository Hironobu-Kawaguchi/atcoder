# https://atcoder.jp/contests/abc116/tasks/abc116_d

n, k = map(int, input().split())
ds = [[] for _ in range(n)] # ネタの種類t(<=n)別においしさdのリスト
for _ in range(n):
    t, d = map(int, input().split())
    t -= 1
    ds[t].append(d)

y0, y1 = [], []
for i in range(n):
    if len(ds[i]) == 0:
        continue
    ds[i].sort()    # 各ネタでおいしさのsort
    y1.append(ds[i][-1])    # 各ネタで最大のおいしさをpopしy1に追加
    ds[i].pop()
    y0.extend(ds[i])        # 各ネタで2番目以降のおいしさのリストをy0に追加
y0.sort(reverse=True)   # ネタの種類が増えないおいしさのリスト（各ネタで2番目以降）を降順sort
y1.sort(reverse=True)   # ネタの種類が増えるおいしさ（各ネタで最大）のリストを降順sort

ans = 0
# Y = max(0, k-len(y0))   # Y: ネタの種類の最小値（kまで増やしながら貪欲するため）
Y = min(k, len(y1))   # Y: ネタの種類の最大値（減らしながら貪欲するため）
X = 0
for i in range(Y):
    X += y1[i]      # Y個 ネタの種類が増えるおいしさ（各ネタで最大）を大きい順に加算
for i in range(k-Y):
    X += y0[i]      # k-Y個 ネタの種類が増えないおいしさを大きい順に加算

while True:
    ans = max(ans, X+Y*Y)
    # if (Y>=k or Y>=len(y1)):   # Yをkまで増やしながら貪欲
    #     break
    # X += y1[Y]      # ネタの種類が増えるおいしさ（各ネタで最大）を大きい順に1つ追加
    # X -= y0[k-Y-1]  # ネタの種類が増えない大きさを小さい順に1つ除外
    # Y += 1
    if (Y<=0 or k-Y>=len(y0)):   # Yを減らしながら貪欲
        break
    X -= y1[Y-1]      # ネタの種類が増えるおいしさ（各ネタで最大）を小さい順に1つ除外
    X += y0[k-Y]  # ネタの種類が増えない大きさを大きい順に1つ追加
    Y -= 1
print(ans)
