# https://atcoder.jp/contests/abc019/tasks/abc019_3

N = int(input())
a = list(map(int, input().split()))
s = set()
for i in range(N):
    tmp = a[i]
    while tmp % 2 == 0:
        tmp /= 2
    s.add(tmp)
ans = len(s)
print(ans)
