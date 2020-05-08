# https://atcoder.jp/contests/tenka1-2013-quala/tasks/tenka1_2013_qualA_b

N = int(input())
ans = 0
for i in range(N):
    vz = list(map(int, input().split()))
    if sum(vz) < 20:
        ans += 1
print(ans)
