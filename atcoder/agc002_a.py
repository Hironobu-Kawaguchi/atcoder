# https://atcoder.jp/contests/agc002/tasks/agc002_a

a, b = map(int, input().split())
if a * b <= 0:
    print("Zero")
elif a < 0 and (a-b+1)%2:
    print("Negative")
else:
    print("Positive")
