# https://atcoder.jp/contests/arc040/tasks/arc040_a

N = int(input())
r, b = 0, 0
for i in range(N):
    S = input()
    for c in S:
        if c == 'R':
            r += 1
        elif c == 'B':
            b += 1

if r > b:
    print("TAKAHASHI")
elif r < b:
    print("AOKI")
else:
    print("DRAW")
    