# https://atcoder.jp/contests/abc008/tasks/abc008_2

N = int(input())
d = dict()
for i in range(N):
    S = input()
    if S in d:
        d[S] += 1
    else:
        d[S] = 1
ans = max(d, key=d.get)
print(ans)
