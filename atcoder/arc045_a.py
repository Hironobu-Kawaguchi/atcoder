# https://atcoder.jp/contests/arc045/tasks/arc045_a

S = list(input().split())
d = {"Left": '<', "Right": '>', "AtCoder": 'A'}
ans = []
for c in S:
    ans.append(d[c])
print(*ans)
