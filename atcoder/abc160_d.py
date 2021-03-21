# https://atcoder.jp/contests/abc160/tasks/abc160_d
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

N, X, Y = map(int, input().split())
ans = [0]*(N-1)
for i in range(N-1):
    for j in range(i+1,N):
        dist = min(j-i, min(abs(X-1-i)+1+abs(Y-1-j), abs(Y-1-i)+1+abs(X-1-j)))
        ans[dist-1] += 1
for i in range(N-1):
    print(ans[i])

# ans = [0]*(N-1)
# branch1 = X-1
# branch2 = N-Y
# cycle = Y-X+1
# for i in range(cycle//2):   # 輪の1/2まで両側(2通り）で行ける
#     ans[i] += cycle
# if cycle%2==0:     # 輪は偶数（両方から同じ距離がある）
#     ans[cycle//2-1] -= cycle//2
# ans[0] -= 1

# for i in range(branch1):
#     for j in range(cycle//2):
#         if cycle%2==0 and j==cycle//2-1:
#             ans[i+j+1] += 1
#         elif j == 0:    # 直線経路は除外
#             ans[i+j+1] += 1
#         else:
#             ans[i+j+1] += 2
# for i in range(branch2):
#     for j in range(cycle//2):
#         if cycle%2==0 and j==cycle//2-1:
#             ans[i+j+1] += 1
#         elif j == 0:    # 直線経路は除外
#             ans[i+j+1] += 1
#         else:
#             ans[i+j+1] += 2

# for i in range(branch1+branch2+1):   # 直線経路
#     ans[i] += branch1+branch2+1 - i

# for i in range(N-1):
#     print(ans[i])

# # X = int(input())
# # S = input()
# # A = list(map(int, (input().split())))
# # A = [[int(i) for i in input().split()] for _ in range(N)]
