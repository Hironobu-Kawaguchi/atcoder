# https://atcoder.jp/contests/abc025/tasks/abc025_a

S = input()
N = int(input())

l = []
for i in range(len(S)):
    for j in range(len(S)):
        l.append(S[i]+S[j])
l.sort()
ans = l[N-1]
print(ans)
