# https://atcoder.jp/contests/arc117/tasks/arc117_c

choice = ['B', 'W', 'R']
c2n = dict(zip(choice, range(3)))
# print(c2n)
n2c = dict(zip(range(3), choice))
# print(n2c)

MAX_N = 400005
bf = [0] * MAX_N    # n! が3で何回割れるか
bg = [0] * MAX_N    # n! を3で割れるだけ割った後の mod 3

for i in range(1, MAX_N):
    pos = i
    while pos%3==0:
        pos //= 3
        bf[i] += 1
    bg[i] = pos%3
bg[0] = 1
for i in range(1, MAX_N):
    bf[i] += bf[i-1]
    bg[i] *= bg[i-1]
    bg[i] %= 3


def nCr_mod3(n, r):
    if bf[n] != bf[r] + bf[n-r]:        return 0
    # if bg[n]==1 and (bg[r]*bg[n-r]==1): return 1
    # if bg[n]==1 and (bg[r]*bg[n-r]==2): return 2
    # if bg[n]==1 and (bg[r]*bg[n-r]==4): return 1
    # if bg[n]==2 and (bg[r]*bg[n-r]==1): return 2
    # if bg[n]==2 and (bg[r]*bg[n-r]==2): return 1
    # if bg[n]==2 and (bg[r]*bg[n-r]==4): return 2
    denom = (bg[r] * bg[n-r])%3
    numer = bg[n]
    if numer < denom:   numer += 3
    if denom!=0:
        return numer // denom
    return -1

N = int(input())
C = input()
# print(C)
# print(bf[:N+1])
# print(bg[:N+1])

# for i in range(N):
#     print(N-1, i, nCr(N-1, i))

A = [c2n[c] for c in C]
# print(A)

ans = 0
for i in range(N):
    ans += A[i] * nCr_mod3(N-1, i)
    ans %= 3
    # print(i, A[i], nCr_mod3(N-1, i), ans)
if N%2==0:
    ans = (3-ans)%3
# print(ans)
print(n2c[ans])




# choice = ['B', 'W', 'R']
# from itertools import product, combinations
# import copy

# def solve(x):
#     now = x
#     for j in range(len(x)-1):
#         next = []
#         for i in range(len(now)-1):
#             if now[i]==now[i+1]:
#                 next.append(now[i])
#             else:
#                 # print(list(choice - set(now[i]) - set(now[i-1]))[0])
#                 # if len(set(choice) - set(now[i]) - set(now[i+1]))!=1:
#                 #     print('ERROR', set(choice) , set(now[i]) , set(now[i+1]))
#                 next.append(list(set(choice) - set(now[i]) - set(now[i+1]))[0])
#         now = copy.copy(next)
#         # print(now)
#     return next[0]

# n = int(input())
# c = input()
# x = list(c)
# # print(n,c,x)
# print(solve(x))

# # print(solve(('B', 'B', 'R')))

# n = 4
# d = {'B':[], 'W':[], 'R':[]}
# for x in product(choice, repeat=n):
#     ans = solve(x)
#     d[ans].append(x)
#     # print(x)
#     # print(solve(x))
#     # break
# for k, v in d.items():
#     print(k, len(v))
#     print(v)



