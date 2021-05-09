# https://atcoder.jp/contests/arc118/tasks/arc118_b

MAXA = 10001
n = int(input())

ans = [1] * n
ans[0] = 2*3
ans[1] = 2*5
ans[2] = 3*5
idx = 3
s = set()
mlt = ans[0]
now = mlt * 2
while now<MAXA:
    s.add(now)
    now += mlt
mlt = ans[1]
now = mlt * 2
while now<MAXA:
    s.add(now)
    now += mlt
mlt = ans[2]
now = mlt * 2
while now<MAXA:
    s.add(now)
    now += mlt

nums = sorted(list(s))
# print(len(nums))
# print(nums)
for i in range(n-3):
    ans[i+3] = nums[i]
print(*ans)

# # check
# from math import gcd
# for i in range(n):
#     for j in range(i+1, n):
#         if ans[i]==ans[j]:
#             print("Error same", i, ans[i], j, ans[j])
#         if gcd(ans[i], ans[j]) == 1:
#             print("Error gcd", i, ans[i], j, ans[j])
# now = ans[-1]
# for i in range(n-1):
#     now = gcd(now, ans[i])
# if now!=1:
#     print("Error gcd all")


# primes = [True] * MAXA
# primes[0] = False
# primes[1] = False
# for i in range(2,4999):
#     baisu = 2*i
#     while baisu < MAXA:
#         primes[baisu] = False
#         baisu += i
# cnt = 0
# prime_list = []
# for i in range(MAXA):
#     if primes[i]:
#         cnt += 1
#         prime_list.append(i)
# print(cnt)
# print(prime_list)
