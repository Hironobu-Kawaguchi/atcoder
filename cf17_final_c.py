# https://atcoder.jp/contests/cf17-final/tasks/cf17_final_c

def f(a, b):
    d = abs(a-b)
    return min(d, 24-d)

N = int(input())
D = list(map(int, input().split())) + [0]
D.sort()
for i in range(N+1):
    if i%2:
        D[i] = 24 - D[i]
D.sort()
ans = f(D[0], D[-1])
for i in range(N):
    ans = min(ans, f(D[i], D[i+1]))
print(ans)
