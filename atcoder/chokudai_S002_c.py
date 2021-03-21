# https://atcoder.jp/contests/chokudai_S002/tasks/chokudai_S002_c

N = int(input())
# A, B = [], []
ans = 0
for i in range(N):
    _a, _b = map(int, input().split())
    # A.append(_a)
    # B.append(_b)
    ans += max(_a, _b)

print(ans)
