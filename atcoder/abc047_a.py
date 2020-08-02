# https://atcoder.jp/contests/abc047/tasks/abc047_a

abc = list(map(int, input().split()))
abc.sort()
if abc[0] + abc[1] == abc[2]:
    print("Yes")
else:
    print("No")
