# https://atcoder.jp/contests/caddi2018/tasks/caddi2018_b

n = int(input())
a = [int(input()) for _ in range(n)]
if all(a[i] % 2 == 0 for i in range(n)):
    print("second")
else:
    print("first")
