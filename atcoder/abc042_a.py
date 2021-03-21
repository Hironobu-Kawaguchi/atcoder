# https://atcoder.jp/contests/abc042/tasks/abc042_a

abc = list(map(int, input().split()))
abc.sort()
if abc == [5, 5, 7]:
    print("YES")
else:
    print("NO")