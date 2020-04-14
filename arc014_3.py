# https://atcoder.jp/contests/arc014/tasks/arc014_3

from collections import Counter
N = int(input())
S = input()

C = Counter(S)
ans = 0
for k in C:
    ans += C[k]%2
print(ans)