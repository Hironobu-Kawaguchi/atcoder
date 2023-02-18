# https://atcoder.jp/contests/arc155/tasks/arc155_a

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

def chk(S):
    n = len(S)
    for i in range(n//2):
        if S[i]!=S[n-1-i]:
            return False
    return True

def main():
    N, K = map(int, input().split())
    S = list(input())
    # print(N, K, S)
    K %= 2 * N
    # print(N, K)
    flg = True
    S_dash = [None]*K
    # print(S_dash)
    for i in range(min(N, K)):
        if S_dash[-i-1] is None:
            S_dash[-i-1] = S[i]
        else:
            if S_dash[-i-1]!=S[i]:
                flg = False
                # print(S_dash, i, S_dash[-i-1], S[i])
        if S_dash[i] is None:
            S_dash[i] = S[-i-1]
        else:
            if S_dash[i]!=S[-i-1]:
                flg = False
                # print(S_dash, i, S_dash[i], S[-i-1])
    # print(S_dash)
    if chk(S + S_dash)==False:
        flg = False
    if chk(S_dash + S)==False:
        flg = False
    if flg:
        print("Yes")
    else:
        print("No")
    return

T = int(input())
for ti in range(T):
    main()



# WA
# import sys
# # input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# # sys.setrecursionlimit(10 ** 7)

# def chk(S):
#     n = len(S)
#     for i in range(n//2):
#         if S[i]!=S[n-1-i]:
#             return False
#     return True

# def chk2(S, M):
#     if M==0:
#         return True
#     k, p = divmod(len(S), M)
#     # print(k, p, S)
#     if p!=0:
#         return False
#     for i in range(1, k):
#         if i%2:
#             if S[:M]!=S[M*i:M*(i+1)][::-1]:
#                 return False
#         else:
#             if S[:M]!=S[M*i:M*(i+1)]:
#                 return False
#     # if p:
#     #     if k%2:
#     #         if S[M-p:M]!=S[k*M:][::-1]:
#     #             return False
#     #     else:
#     #         if S[M-p:M]!=S[k*M:]:
#     #             return False
#     return True

# def main():
#     N, K = map(int, input().split())
#     S = input()
#     # print(N, K, S)
#     Q, M = divmod(K, N)
#     # print(K, N, Q, M)
#     # if chk(S[:N-M]) and chk(S[M:]) and S[:M]==S[N-M:]:
#     if chk(S[:N-M]) and chk(S[M:]) and chk2(S, M):
#     # if chk(S[:N-M]) and chk(S[M:]) and chk2(S, M) and chk2(S[::-1], M):
#         print("Yes")
#         return
#     # if chk(S[:N-M]) and chk(S[M:]):
#     # if chk(S[:N-M]) and chk(S[M:]) and S[:M]==S[N-M:]:
#     #     print("Yes")
#     #     return
#     print("No")
#     return

# T = int(input())
# for ti in range(T):
#     main()

