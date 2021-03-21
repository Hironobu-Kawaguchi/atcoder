# https://atcoder.jp/contests/abc071/tasks/abc071_b

import string
S = input()
al = string.ascii_lowercase

for a in al:
    if a not in S:
        print(a)
        break
else:
    print('None')

