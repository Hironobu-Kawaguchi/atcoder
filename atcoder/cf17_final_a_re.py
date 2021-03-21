# https://atcoder.jp/contests/cf17-final/tasks/cf17_final_a

import re
s = input()
if re.match('A?KIHA?BA?RA?$', s):
    print('YES')
else:
    print('NO')
