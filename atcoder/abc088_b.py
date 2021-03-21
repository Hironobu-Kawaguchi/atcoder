# https://atcoder.jp/contests/language-test-202001/tasks/abc088_b

N = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
ans = 0
for i in range(N):
    if (i&1)==0:    # i:偶数 -> 奇数番目 -> Alice
        ans += a[i]
    else:           # Bob
        ans -= a[i]
print(ans)
