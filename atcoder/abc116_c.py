# C - Grand Garden
# https://atcoder.jp/contests/abc116/tasks/abc116_c

N = int(input())
h = list(map(int, input().split()))

nums = [h[0]]

for i in range(N-1):
    if h[i+1] > h[i]:
        nums.append(nums[i] + (h[i+1] - h[i]))
    else:
        nums.append(nums[i])

print(nums[-1])
# print(nums)
