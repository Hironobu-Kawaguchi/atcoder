# https://atcoder.jp/contests/arc052/tasks/arc052_a

S = input()
from string import digits

ans = ''
for s in S:
    if s in digits:
        ans += s
print(ans)
