# https://atcoder.jp/contests/abc050/tasks/arc066_a

MOD = 1000000007
import collections
N = int(input())
A = list(map(int, input().split()))
c = collections.Counter(A)

def chk(c, n):
    if n % 2:
        if 0 not in c or c[0] != 1:
            return False
        for i in range(2, (n//2)*2+1, 2):
            if i not in c or c[i] != 2:
                return False
    else:
        for i in range(1, n, 2):
            if i not in c or c[i] != 2:
                return False
    return True

if chk(c, N):
    ans = 2 ** (N//2) % MOD
else:
    ans = 0

print(ans)
