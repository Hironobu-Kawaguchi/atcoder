# https://atcoder.jp/contests/agc015/tasks/agc015_a

N, A, B = map(int, input().split())

if A > B:
    ans = 0
elif N == 1 and A != B:
    ans = 0
elif N <= 2:
    ans = 1
else:
    mn = A * (N-1) + B
    mx = A + B * (N-1)
    ans = mx - mn + 1
print(ans)
