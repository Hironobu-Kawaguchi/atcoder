# https://atcoder.jp/contests/abc137/tasks/abc137_a

N = int(input())
ss = []
for i in range(N):
    s = list(input())
    s.sort()
    ss.append(s)

ss.sort()
ans = 0
tmp = 1
for i in range(N-1):
    if ss[i] == ss[i+1]:
        tmp += 1
        if i == N-2:
            ans += (tmp * (tmp-1)) // 2
    else:
        ans += (tmp * (tmp-1)) // 2
        tmp = 1

print(ans)
