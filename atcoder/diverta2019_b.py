# https://atcoder.jp/contests/diverta2019/tasks/diverta2019_b

R, G, B, N = map(int, input().split())
ans = 0

for r in range(N//R+1):
    tmp = N - r * R
    for g in range(tmp//G+1):
        if (N - r * R - g * G) % B == 0:
            ans += 1

print(ans)
