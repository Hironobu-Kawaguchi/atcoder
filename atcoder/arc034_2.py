# https://atcoder.jp/contests/arc034/tasks/arc034_2
import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

N = int(input())

def f(x):
    res = 0
    while x>0:
        res += x%10
        x //= 10
    return res

MAX = 9 * 18
start = max(1, N - MAX)
k = 0
ans = []
for x in range(start, N+1):
    if x + f(x) == N:
        k += 1
        ans.append(x)
print(k)
for x in ans:
    print(x)
