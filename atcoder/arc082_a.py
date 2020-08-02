# https://atcoder.jp/contests/abc072/tasks/arc082_a

N = int(input())
a = list(map(int, input().split()))
MAX_a = 10**5 + 1
l = [0] * (MAX_a)

for i in range(N):
    l[a[i]] += 1

tmp = l[0] + l[1] + l[2]
ans = tmp
for i in range(3, MAX_a):
    tmp = tmp + l[i] - l[i-3]
    ans = max(tmp , ans)

print(ans)
