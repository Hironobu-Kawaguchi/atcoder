# https://atcoder.jp/contests/abc161/tasks/abc161_d
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

K = int(input())
nums = []
def make_num(keta, str_num):
    if len(str_num) == keta:
        nums.append(str_num)
        return
    if str_num[-1] == '0':
        # for i in [0,1,9]:
        for i in [0,1]:
            make_num(keta, str_num + str(i))
    elif str_num[-1] == '9':
        # for i in [0,8,9]:
        for i in [8,9]:
            make_num(keta, str_num + str(i))
    else:
        for i in range(-1, 2):
            make_num(keta, str_num + str(int(str_num[-1])+i))

def enum(keta):
    for i in range(1,10):
        make_num(keta, str(i))

keta = 0
while len(nums) < K:
    keta += 1
    enum(keta)

# print(nums[K-20:])
print(nums[K-1])

# TLE
# def chk(num):
#     s = str(num)
#     for i in range(len(s)-1):
#         if abs(int(s[i]) - int(s[i+1])) > 1:
#             return False
#     return True

# K = int(input())
# cnt = 0
# now = 0
# while cnt < K:
#     now += 1
#     if chk(now):
#         cnt += 1
# print(now)

# S = input()
# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
