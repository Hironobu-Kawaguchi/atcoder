# B - Palace
# https://atcoder.jp/contests/abc113/tasks/abc113_b

N = int(input())
T, A  = map(int, input().split())
H = list(map(int, input().split()))

dif = []
for i in range(N):
    temp = T - H[i] * 0.006
    dif.append(abs(A - temp))

ans = dif.index(min(dif)) + 1
print(ans)
