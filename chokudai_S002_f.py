# https://atcoder.jp/contests/chokudai_S002/tasks/chokudai_S002_f

N = int(input())
# A, B = [], []
s = set()
for i in range(N):
    a, b = map(int, input().split())
    # A.append(_a)
    # B.append(_b)
    if a > b:
        s.add((a,b))
    else:
        s.add((b,a))

ans = len(s)
print(ans)
