# 
# https://atcoder.jp/contests/abc129/tasks/abc129_c


N, M = map(int, input().split())
s = set()
for i in range(M):
    s.add(int(input()))
l = [0, 1]
for i in range(1, N+1):
    if i in s:
        l.append(0)
    else:
        tmp = (l[-1] + l[-2]) % 1000000007
        l.append(tmp)

ans = l[-1]
# print(l)
print(ans)

