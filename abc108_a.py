# A - Pair
# https://atcoder.jp/contests/abc108/tasks/abc108_a

K = int(input())

ans = K // 2
ans = (K- ans) * ans
print(ans)
