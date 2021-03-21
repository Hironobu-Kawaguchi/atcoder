# https://atcoder.jp/contests/abc085/tasks/abc085_c

N, Y = map(int, input().split())
ans = [-1, -1, -1]
for x in range(N+1):
    if 10000 * x > Y:
        break
    for y in range(N+1):
        if 10000 * x + 5000 * y > Y:
            break
        if 10000 * x + 5000 * y + 1000 * (N-x-y) == Y:
            ans = [x, y, N-x-y]
print(*ans)
