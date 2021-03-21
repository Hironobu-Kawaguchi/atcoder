# https://atcoder.jp/contests/agc036/tasks/agc036_a

S = int(input())
x1 = 10**9
y1 = 1
y2, x2 = divmod(S, x1)
if x2 != 0:
    x2 = x1 - x2
    y2 +=1
print(x1, y1, x2, y2, 0, 0)
