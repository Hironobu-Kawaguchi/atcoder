# https://atcoder.jp/contests/abc027/tasks/abc027_a

l = list(map(int, input().split()))
if l[0] == l[1]:
    ans = l[2]
elif l[1] == l[2]:
    ans = l[0]
elif l[2] == l[0]:
    ans = l[1]
print(ans)
