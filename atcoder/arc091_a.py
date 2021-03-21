# https://atcoder.jp/contests/abc090/tasks/arc091_a

N, M = map(int, input().split())

if N == 1 and M == 1:
    ans = 1
elif N == 1:
    ans = M - 2
elif M == 1:
    ans = N - 2
else:
    ans = (N-2) * (M-2)
print(ans)


# N, M = map(int, input().split())

# if N == 2 or M == 2:
#     ans = 0
# elif N == 1 and M == 1:
#     ans = 1
# elif N == 1:
#     ans = M - 2
# elif M == 1:
#     ans = N - 2
# else:
#     ans = (N-2) * (M-2)
# print(ans)
