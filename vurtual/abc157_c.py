# https://atcoder.jp/contests/abc157/tasks/abc157_c
import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

def main():
    N, M = map(int, input().split())
    nums = [-1] * N
    for i in range(M):
        s, c = map(int, input().split())
        s -= 1
        if s == 0 and c == 0 and N>1:
            print(-1)
            return
        elif nums[s] == -1:
            nums[s] = c
        elif nums[s] != c:
            print(-1)
            return
    if M == 0:
        if N==1:
            nums[0] = 0
        else:
            nums[0] = 1
    ans = ''
    for i in range(N):
        if nums[i] == -1:
            if i==0:
                ans += '1'
            else:
                ans += '0'
        else:
            ans += str(nums[i])
    print(ans)

main()


# A = [[int(i) for i in input().split()] for _ in range(3)]
# N = int(input())
# b = [int(input()) for _ in range(N)]
# S = input()
# l = list(map(int, (input().split())))
