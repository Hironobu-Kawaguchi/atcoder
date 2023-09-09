# https://atcoder.jp/contests/abc319/tasks/abc319_b

INF = 1001001001

N = int(input())

js = []
for j in range(1, 10):
    if N%j==0:
        js.append(j)
# print(js)

s = []
for i in range(N+1):
    now = INF
    for j in js:
        if i%(N//j)==0:
            now = min(now, j)
    if now==INF:
        s.append("-")
    else:
        s.append(str(now))
print("".join(s))