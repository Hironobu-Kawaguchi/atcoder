# https://atcoder.jp/contests/abc105/tasks/abc105_b

N = int(input())

ans = "No"
for i in range(N//4+1):
    if (N - i * 4) % 7 == 0:
        ans = "Yes"
        break

print(ans)
