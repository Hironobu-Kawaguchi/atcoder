# https://atcoder.jp/contests/chokudai_S002/tasks/chokudai_S002_h

N = int(input())
# A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    # A.append(_a)
    # B.append(_b)
    if a == b:
        ans = -1
    else:
        tmp = max(a, b)
        for i in range(tmp, 0, -1):
            if a % i == b % i:
                ans = i
                break
    print(ans)
