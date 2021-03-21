# https://atcoder.jp/contests/arc033/tasks/arc033_2

na, nb = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

ans = len(a & b) / len(a | b)
print(ans)
