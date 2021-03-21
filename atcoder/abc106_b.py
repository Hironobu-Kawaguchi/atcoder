# B - 105
# https://atcoder.jp/contests/abc106/tasks/abc106_b
# 105 : 1, 3, 5, 7, 15, 21, 35, 105

N = int(input())
ans = 0
for i in range(1, N+1, 2):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 8:
        ans += 1

print(ans)
