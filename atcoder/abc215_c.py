# https://atcoder.jp/contests/abc215/tasks/acc215_c


from itertools import permutations
S, K = input().split()
K = int(K)
st = set()
for x in permutations(S):
    st.add(x)
ss = sorted(list(st))
print(''.join(ss[K-1]))


# import sys
# from collections import Counter
# sys.setrecursionlimit(10 ** 7)

# def count(s):
#     cnt = Counter(s)
#     n = len(s)
#     ret = 1
#     for i in range(2, n+1):
#         ret *= i
#     for k, v in cnt.items():
#         for i in range(2, v+1):
#             ret //= i
#     return ret

# def remove_c(s, c):
#     removec = []
#     flg = True
#     for cc in s:
#         if flg and cc==c:
#             flg = False
#         else:
#             removec.append(cc)
#     return removec

# def solve(s, k, prefix=''):
#     if len(s)==1: return prefix + s[0]
#     sets = set(s)
#     cum = 0
#     for c in sorted(list(sets)):
#         removec = remove_c(s, c)
#         add_cnt = count(removec)
#         if cum+add_cnt>=k:
#             # print(removec, k-cum, prefix+c)
#             return solve(removec, k-cum, prefix+c)
#         cum += add_cnt
#     return

# S, K = input().split()
# S = list(S)
# K = int(K)
# # print(count(S))
# ans = solve(S, K, prefix='')
# print(ans)

