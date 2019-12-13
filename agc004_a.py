# https://atcoder.jp/contests/agc004/tasks/agc004_a

abc = list(map(int, input().split()))
abc.sort()
if abc[0]%2==0 or abc[1]%2==0 or abc[2]%2==0:
    print(0)
else:
    print(abc[0]*abc[1])
