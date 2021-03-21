# B - カキ
# https://abc029.contest.atcoder.jp/tasks/abc029_b

import sys
ans = 0
for line in sys.stdin.readlines():
    if 'r' in line:
        ans += 1
print(ans)
