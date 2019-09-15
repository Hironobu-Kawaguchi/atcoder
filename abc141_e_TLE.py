# https://atcoder.jp/contests/abc141/tasks/abc141_e
# TLE
N = int(input())
S = input()

ans = 0
for i in range(N-1):
    for j in range(i+1+ans, N-ans):
        for l in range(ans+1, min(j-i, N-j)+1):
            if S[i:i+l] == S[j:j+l]:
                ans = max(ans, l)
            else:
                break

print(ans)
