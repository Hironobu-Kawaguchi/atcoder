# https://atcoder.jp/contests/nomura2020/tasks/nomura2020_a
import sys
# def input(): return sys.stdin.readline().rstrip()
# input = sys.stdin.readline
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

H1, M1, H2, M2, K = map(int, input().split())
ans = (H2*60+M2) - (H1*60+M1)
if ans < 0:
    ans += 24*60
ans = max(ans - K, 0)
print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
