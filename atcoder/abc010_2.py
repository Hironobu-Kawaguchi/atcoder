# https://atcoder.jp/contests/abc010/tasks/abc010_2

n = int(input())
a = list(map(int, input().split()))
dic = {1:0, 2:1, 3:0, 4:1, 5:2, 0:3}
ans = 0
for i in range(n):
    ans += dic[a[i] % 6]
print(ans)
