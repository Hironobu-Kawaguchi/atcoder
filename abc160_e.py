# https://atcoder.jp/contests/abc160/tasks/abc160_d
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

X, Y, A, B, C = map(int, input().split())
cand = []
p = list(map(int, (input().split())))
p.sort(reverse=True)
cand.extend(p[:X])
q = list(map(int, (input().split())))
q.sort(reverse=True)
cand.extend(q[:Y])
r = list(map(int, (input().split())))
cand.extend(r)
cand.sort(reverse=True)
ans = sum(cand[:X+Y])
print(ans)


# X = int(input())
# S = input()
# A = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
