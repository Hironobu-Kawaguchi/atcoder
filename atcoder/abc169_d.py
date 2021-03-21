# https://atcoder.jp/contests/abc169/tasks/abc169_d

# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

from collections import Counter
N = int(input())

#nを素因数分解したリストを返す
def prime_decomposition(n):
  i = 2
  table = []
  while i * i <= n:
    while n % i == 0:
      n //= i
      table.append(i)
    i += 1
  if n > 1:
    table.append(n)
  return table

def unique_count(n):
    res = 0
    while n>=0:
        res += 1
        n -= res
    # print(res)
    return res-1

Cnt = Counter(prime_decomposition(N))
# print(Cnt)
ans = 0
for c in Cnt.values():
    ans += unique_count(c)
print(ans)

# N = int(input())
# S = input()
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
