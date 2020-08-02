# B - Tree Burning
# https://atcoder.jp/contests/agc030/tasks/agc030_b

l, n = map(int, input().split())
x = [int(input()) for _ in range(n)]

"""
l, n = map(int, input().split())
x = [int(input()) for _ in range(n)]
tmp = 0
left = 0
right = -1
ans = 0

for i in range(n):
    dleft = x[left] - tmp if tmp < x[left] else x[left] - tmp + l
    dright = tmp - x[right] if tmp > x[right] else l - x[right] + tmp
    if dleft > dright:
        ans += dleft
        tmp = x[left]
        left += 1
    else:
        ans += dright
        tmp = x[right]
        right -= 1
    print(tmp, ans, left, right, dleft, dright)

print(ans)
"""