# https://atcoder.jp/contests/judge-update-202004/tasks/judge_update_202004_c
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

from itertools import permutations

a = list(map(int, input().split()))
N = sum(a)

def chk(num_list):
    nums = [[99]*4 for _ in range(4)]
    for i in num_list:
        if i < a[0]:
            nums[0][i] = num_list[i]
        elif i < a[0]+a[1]:
            nums[1][i-a[0]] = num_list[i]
        else:
            nums[2][i-a[0]-a[1]] = num_list[i]
    for i in range(3):
        for j in range(3):
            if nums[i][j] > nums[i][j+1]:
                return False
            if nums[i][j] > nums[i+1][j]:
                return False
    return True

ans = 0
for p in permutations(range(1,N)):
    num_list = [0] + list(p)
    if chk(num_list):
        ans += 1
print(ans)

# S = input()
# N = int(input())
# S, L, R = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
