# C - ID
# https://atcoder.jp/contests/abc113/tasks/abc113_c

N, M  = map(int, input().split())

pys = []
for i in range(M):
    p, y = map(int, input().split())
    pys.append([p, y, i])

nums = [0] * N
ans = [''] * M
pys.sort(key=lambda x:x[1])

for p, y, i in pys:
    nums[p-1] += 1
    ans[i] = str(p).zfill(6) + str(nums[p-1]).zfill(6)

for an in ans:
    print(an)
