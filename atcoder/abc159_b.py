# https://atcoder.jp/contests/abc159/tasks/abc159_a
import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

S = input()
n = len(S)

def kaibun(s):
    n = len(s)
    for i in range(n//2):
        if s[i] != s[-1-i]:
            return False
    return True

if kaibun(S) and kaibun(S[:n//2]) and kaibun(S[n//2+1:]):
    print("Yes")
else:
    print("No")


# N, M = map(int, input().split())
# ans = (N+M)*(N+M-1)//2 - N*M
# print(ans)

# n = int(input())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
