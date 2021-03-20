# https://atcoder.jp/contests/abc196/tasks/abc196_c

# N = int(input())
# ans = 0
# for i in range(1, 1000001):
#     x = int(str(i)*2)
#     if x<=N: ans += 1
# print(ans)

N = int(input())
ans = 0
# for keta in range(1,6):   # WA
for keta in range(1,7):
    for nums in range(10**(keta-1), 10**keta):
        x = nums * (10**keta) + nums
        if x<=N: ans += 1
print(ans)


# Check
# def good(N):
#     # N = int(input())
#     ans = 0
#     for i in range(1, 1000001):
#         x = int(str(i)*2)
#         if x<=N: ans += 1
#     # print(ans)
#     return ans
# 
# def WA(N):
#     # N = int(input())
#     ans = 0
#     for keta in range(1,6):
#         for nums in range(10**(keta-1), 10**keta):
#             x = nums * (10**keta) + nums
#             if x<=N: ans += 1
#     # print(ans)
#     return ans
# 
# import random
# while True:
#     i = random.randint(1, 1000000000000)
#     if good(i)!=WA(i):
#         print(i)
#         break
