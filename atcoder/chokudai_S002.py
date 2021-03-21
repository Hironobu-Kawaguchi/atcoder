# https://atcoder.jp/contests/chokudai_S002

N = int(input())
# A, B = [], []
for i in range(N):
    _a, _b = map(int, input().split())
    # A.append(_a)
    # B.append(_b)
    ans = _a * _b
    print(ans)
