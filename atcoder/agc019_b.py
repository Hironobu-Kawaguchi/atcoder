# https://atcoder.jp/contests/agc019/tasks/agc019_b

from collections import defaultdict
A = input()
n = len(A)
ans = 1
cnt = defaultdict(int)
for i in range(n):
    ans += i - cnt[A[i]]    # iの累計 n*(n-1)/2
    cnt[A[i]] += 1
print(ans)
