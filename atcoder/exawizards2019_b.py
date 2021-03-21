# https://atcoder.jp/contests/exawizards2019/tasks/exawizards2019_b

N = int(input())
s = input()
r, b = 0, 0
for i in range(N):
    if s[i] == 'R':
        r += 1
    else:
        b += 1
if r > b:
    print("Yes")
else:
    print("No")
