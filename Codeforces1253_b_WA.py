# https://codeforces.com/contest/1253/problem/B
# Codeforces Round #600 (Div. 2)

n = int(input())
a = list(map(int, input().split()))

days = 1
ans = []
dp = [0] * 1000001
j = 0
for i, x in enumerate(a):
    if x > 0:
        if dp[x] == 0:
            dp[x] = 1
        elif dp[x] == 1:
            days = -1
            break
        else:
            days += 1
            dp = [0] * 1000001
            dp[x] = 1
            ans.append(i-j)
            j = i
    elif x < 0:
        if dp[-x] == 0:
            days = -1
            break
        elif dp[-x] == 1:
            dp[-x] = 2
        else:
            days = -1
            break
ans.append(i+1-j)

print(days)
if days != -1:
    print(*ans)
