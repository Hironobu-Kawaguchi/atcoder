# https://atcoder.jp/contests/agc060/tasks/agc060_a

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
MOD = 998244353

def main():
    N = int(input())
    S = input()
    # print(S)

    dp = [[[0]*26 for _ in range(26)] for _ in range(N)]

    def ok(i, v):
        if S[i]=='?': return True
        else: return ord(S[i]) - ord('a')==v

    for x in range(26):
        for y in range(26):
            # print(x, y, x!=y, ok(0,x), ok(1,y))
            if x!=y and ok(0,x) and ok(1,y):
                dp[1][x][y] = 1
    # print(dp[0])
    
    for i in range(2, N):
        for x in range(26):
            for y in range(26):
                for z in range(26):
                    if x!=z and y!=z and ok(i,z):
                        dp[i][y][z] += dp[i-1][x][y]
                        dp[i][y][z] %= MOD

    ans = 0
    for x in range(26):
        for y in range(26):
            ans += dp[N-1][x][y]
            ans %= MOD
    print(ans)

main()


# TLE
# from itertools import product
# from string import ascii_lowercase
# d = dict(zip(ascii_lowercase, range(26)))
# # print(d)
# MOD = 998244353

# N = int(input())
# S = input()
# lst = list(S)
# # print(lst)

# num_hatena = 0
# idx_hatena = []
# for i in range(N):
#     if lst[i]=='?':
#         num_hatena += 1
#         idx_hatena.append(i)

# def chk(lst):
#     cum = [[0]*26 for _ in range(N+1)]
#     for i in range(N):
#         for k in range(26):
#             cum[i+1][k] = cum[i][k]
#         cum[i+1][d[lst[i]]] += 1
#     for i in range(N-1):
#         for j in range(i+1, N):
#             for k in range(26):
#                 if (cum[j+1][k]-cum[i][k])*2>j+1-i:
#                     return False
#     return True

# ans = 0
# for x in product(ascii_lowercase, repeat=num_hatena):
#     # print(x)
#     for idx, c in enumerate(x):
#         lst[idx_hatena[idx]] = c
#     # print(chk(lst), lst)
#     if chk(lst):
#         ans += 1
#         ans %= MOD
# print(ans)
