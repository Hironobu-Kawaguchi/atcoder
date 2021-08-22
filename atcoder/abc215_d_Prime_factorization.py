# https://atcoder.jp/contests/abc215/tasks/acc215_d

N, M = map(int, input().split())
A = list(map(int, (input().split())))
L = 100001
x = [False] * L
for i in range(N):
    x[A[i]] = True

d = []
for i in range(2, L):
    flag = False
    for j in range(i, L, i):
        if x[j]:
            flag = True
            break
    if flag: d.append(i)

ok = [True] * (M+1)
for i in d:
    for j in range(i, M+1, i):
        ok[j] = False

cnt = 0
for i in range(1, M+1):
    if ok[i]:
        cnt += 1
print(cnt)
for i in range(1, M+1):
    if ok[i]:
        print(i)


# import math
# import collections
# def prime_factor_table(n):
#     table = [0] * (n + 1)
    
#     for i in range(2, n + 1):
#         if table[i] == 0:
#             for j in range(i + i, n + 1, i):
#                 table[j] = i
    
#     return table

# def prime_factor(n, prime_factor_table):
#     prime_count = collections.Counter()
    
#     while prime_factor_table[n] != 0:
#         prime_count[prime_factor_table[n]] += 1
#         n //= prime_factor_table[n]
#     prime_count[n] += 1
    
#     return prime_count

# N, M = map(int, input().split())
# A = list(map(int, (input().split())))
# MAXA = M
# for a in A:
#     if a>MAXA: MAXA = a
# table = prime_factor_table(MAXA)

# factorization = set()
# for a in A:
#     if a<2: continue
#     factorization |= set(prime_factor(a, table))
# # print(factorization)
# ans = [1]
# for k in range(2, M+1):
#     kfact = set(prime_factor(k, table))
#     # print(k, kfact, factorization)
#     if kfact.isdisjoint(factorization):
#         ans.append(k)
# print(len(ans))
# for k in ans:
#     print(k)
