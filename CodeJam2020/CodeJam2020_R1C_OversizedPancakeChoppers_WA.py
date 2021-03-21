# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef2/00000000002d5b62
# D<=3 なら2以下であり、0か1かをチェック

from collections import Counter

def solve():
    N, D = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    ret = D-1
    double = []
    c = Counter(A)
    for k in c:
        if c[k] >= D:
            return 0
        if c[k] == 2:
            double.append(k)
    if double:  # 2個以上がある
        double.sort()
        if double[0] < A[-1]:   # 最大値ではない2個以上があれば、最大を1回切れば3個になる
            return 1
    s = set(A)
    for i in range(N-1, 0, -1):
        if A[i]%2==0 and A[i]//2 in s:
            return 1
    return ret

T = int(input())
for x in range(T):
    y = solve()
    print('Case #{}:'.format(x + 1), y)
