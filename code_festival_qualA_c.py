# https://atcoder.jp/contests/code-festival-2014-quala/tasks/code_festival_qualA_c

A, B = map(int, input().split())
ans = B//4 - (A-1)//4
ans -= B//100 - (A-1)//100
ans += B//400 - (A-1)//400
print(ans)
