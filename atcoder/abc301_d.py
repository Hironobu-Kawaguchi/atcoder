# https://atcoder.jp/contests/abc301/tasks/abc301_d

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

# S = list(reversed(input().rstrip()))
# N = int(input())    # 10**18
# ans = 0
# for i in range(len(S)):
#     ans |= (S[i]=='1') << i     ### とりあえず?を0にしてみる
# if ans > N:
#     print(-1)   ### 全部0だった場合にNを超える場合は-1
# else:
#     for i in reversed(range(len(S))):     ### 上位の桁から見ていく
#         if S[i]=='?' and (ans | (1<<i)) <= N:   ### 1にしてもNを超えない場合
#             ans |= (1<<i)   ### 1にする
#     print(ans)

S = list(reversed(input().rstrip()))
N = int(input())    # 10**18

def solve(S, N):
    # 桁DP
    dp = [[-1] * 2 for _ in range(len(S)+1)]    ### 0: min, 1: max
    dp[-1][1] = 0
    for i in reversed(range(len(S))):   ### 上位の桁から見ていく
        for j in range(2):  # j: DPで1つ前のmin, max
            if dp[i+1][j]==-1: continue     # 既にNを超えているのでダメ
            if S[i]=='?':   # ?の場合は0, 1両方試す
                for k in range(2):
                    if dp[i+1][j] | (k << i) <= N:   # Nを超えている場合はダメ
                        dp[i][k] = max(dp[i][k], dp[i+1][j] | (k << i))   # 既にあるものより大きい場合のみ更新
            else:   # ?以外の場合はそのまま
                if dp[i+1][j] | (int(S[i]) << i) <= N:   # Nを超えている場合はダメ
                    dp[i][j] = max(dp[i][j], dp[i+1][j] | (int(S[i]) << i))   # 既にあるものより大きい場合のみ更新
        if dp[i][0]==-1 and dp[i][1]==-1:   # 両方ともダメな場合は-1
            # print(i, dp)
            ans = -1
            print(ans)
            return ans
    # print(dp)
    ans = max(dp[0])  # 最後の桁の0, 1の大きい方
    print(ans)
    return ans

ans = solve(S, N)

# def chk(S, N, ans):
#     from itertools import product
#     from bisect import bisect_right
#     cntq = 0
#     for s in S:
#         if s=='?':
#             cntq += 1
#     T = []
#     for bit in product([0, 1], repeat=cntq):
#         bit = list(bit)
#         bitT = ''
#         for s in reversed(S):
#             if s=='?':
#                 bitT += str(bit.pop())
#             else:
#                 bitT += s
#         t = int(bitT, 2)
#         T.append(t)
#     T.sort()
#     idx = bisect_right(T, N)
#     if idx==0:
#         anst = -1
#     else:
#         anst = T[idx-1]
#     print(ans, anst, T)
#     if ans!=anst:
#         print(bin(ans), bin(anst))
#         return False, anst
#     return True, anst

# print(chk(S, N, ans))

# for _ in range(10000):
#     import random
#     S = [random.choice(['0', '1', '?']) for _ in range(16)]
#     # print(S)
#     # N = random.randint(1, 10e18)
#     N = random.randint(1, 10e3)
#     # print(N)
#     ans = solve(S, N)
#     flg, anst = chk(S, N, ans)
#     if not flg:
#         print("error:", ''.join(reversed(S)), N, ans, anst)
#         break
#     # else:
#     #     print("ok:", ''.join(reversed(S)), N, ans, anst)
