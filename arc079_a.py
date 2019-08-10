# https://atcoder.jp/contests/abc068/tasks/arc079_a

N, M = map(int, input().split())

l = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    l[a].append(b)
    l[b].append(a)
ans = 'IMPOSSIBLE'
for i in l[0]:
    for j in l[i]:
        if j == N-1:
            ans = 'POSSIBLE'
            break
print(ans)
