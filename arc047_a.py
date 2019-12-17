# https://atcoder.jp/contests/arc047/tasks/arc047_a

N, L = map(int, input().split())
S = input()

ans, num = 0, 1
for i in range(N):
    if S[i] == '+':
        num += 1
    else:
        num -= 1
    if num > L:
        ans += 1
        num = 1

print(ans)
