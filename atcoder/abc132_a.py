# https://atcoder.jp/contests/abc132/tasks/abc132_a

import collections
S = input()

cnt = collections.Counter(S)

ans = 'Yes'
if len(cnt) == 2:
    for value in cnt.values():
        if value != 2:
            ans = 'No'
else:
    ans = 'No'

print(ans)
