# https://atcoder.jp/contests/abc324/tasks/abc324_d

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
S = list(input())
max_S = int("".join(sorted(S, reverse=True)))
# print(max_S)
S.sort()
# print(S)

ans = 0
now = 0
while now*now<=max_S:
    t = list(str(now * now))
    t.extend(["0"]*(N-len(t)))
    t.sort()
    if t==S:
        ans += 1
    now += 1
print(ans)
