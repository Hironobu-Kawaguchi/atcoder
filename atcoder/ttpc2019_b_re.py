# https://atcoder.jp/contests/ttpc2019/tasks/ttpc2019_b

import re
pattern = '.*okyo.*ech.*'
# repattern = re.compile(pattern)

N = int(input())
for i in range(N):
    s = input()
    if re.match(pattern, s):
        print("Yes")
    else:
        print("No")
