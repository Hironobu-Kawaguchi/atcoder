# https://atcoder.jp/contests/chokudai_S002/tasks/chokudai_S002_b

N = int(input())
# A, B = [], []
for i in range(N):
    _a, _b = map(int, input().split())
    # A.append(_a)
    # B.append(_b)
    ans = _a % _b
    print(ans)
