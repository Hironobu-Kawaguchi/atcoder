# C - To Infinity
# https://atcoder.jp/contests/abc106/tasks/abc106_c

S = input()
K = int(input())

for i in range(K):
    if S[i] != '1':
        ans = S[i]
        break
    elif i == K - 1:
        ans = S[i]

print(ans)
