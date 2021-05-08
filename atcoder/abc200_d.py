# https://atcoder.jp/contests/abc200/tasks/abc200_d

n = int(input())
a = list(map(int, (input().split())))
b, c = [], []
dp = [[] for _ in range(200)]
for i in range(n):
    a[i] %= 200
    for j in range(200):
        if len(dp[j])==0: continue
        if dp[j][-1]==i+1: continue
        next = (j + a[i])%200
        if len(dp[next])>0:
            b = dp[next]
            c = dp[j] + [i+1]
            break
        else:
            dp[next].extend(dp[j] + [i+1])
    if len(dp[a[i]])>0:
        b = dp[a[i]]
        c = [i+1]
        break
    else:
        dp[a[i]].append(i+1)
    if len(b)>0:
        break
if len(b)>0:
    print("Yes")
    print(len(b), *b)
    print(len(c), *c)
else:
    print("No")
# print(dp)

# mod200 = 0
# for i in b:
#     mod200 += a[i-1]
#     mod200 %= 200
# print('b', mod200)

# mod200 = 0
# for i in c:
#     mod200 += a[i-1]
#     mod200 %= 200
# print('c', mod200)


