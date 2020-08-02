# https://atcoder.jp/contests/abc140/tasks/abc140_d

N, K = map(int, input().split())
S = input()

tmp = 0
pre = ''
for i in range(N):
    if S[i] != pre:
        tmp += 1
        pre = S[i]
ans = min(N-1, N-tmp+2*K)
print(ans)

# nums = []
# tmp = 0
# pre = 'L'
# for i in range(N):
#     if S[i] == pre:
#         tmp += 1
#     else:
#         nums.append(tmp)
#         tmp = 1
#         pre = S[i]
# nums.append(tmp)
# if S[-1] == 'L':
#     nums.append(0)

# sums = [0]
# for i in range(len(nums)):
#     sums.append(sums[-1] + nums[i])
# print(sums)
# sumsk = []
# for i in range(len(sums)-2*K):
#     sumsk.append(sums[i+2*K] - sums[i])
# print(sumsk)

# Ls, Rs = [0], [0]
# Lsum, Rsum = 0, 0
# # Lsum, Rsum = nums[0]-1, nums[1]-1
# for i in range(len(nums)//2):
#     Ls.append(Ls[-1] + nums[2*i+1])
#     Rs.append(Rs[-1] + nums[2*i])
#     Lsum += nums[2*i] - 1
#     Rsum += nums[2*i+1] - 1
# # Rs.append(nums[-2])

# ans = 0

# print(nums)
# print(Lsum, Ls)
# print(Rsum, Rs)
# # ans = B[0] + B[-1]
# # print(ans)
