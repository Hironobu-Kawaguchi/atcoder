# E - 「く」
# https://atcoder.jp/contests/iroha2019-day3/tasks/iroha2019_day3_e

N = int(input())
C = [input() for _ in range(N)]

ans = 0

nums = []
tmpc = '/'
tmpn = 0
for c in C:
    if c == tmpc:
        tmpn += 1
    else:
        nums.append(tmpn)
        tmpn = 1
    tmpc = c
nums.append(tmpn)

ans = 0
for i in range(0, len(nums)//2 * 2, 2):
    if nums[i] == nums[i+1]:
        ans += 1

print(ans)
