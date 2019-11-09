# https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_c

import numpy as np
N = int(input())
A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))
cnt = np.count_nonzero(A>B)

if cnt > (N-2)*2:
    print("No")
elif all(np.sort(A) <= np.sort(B)):
    print("Yes")
else:
    print("No")
