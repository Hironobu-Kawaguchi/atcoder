# https://codeforces.com/contest/1459/problem/A

import sys
sys.setrecursionlimit(10 ** 7)
import copy

MAXN = 1001
fact = [1]
for i in range(MAXN):
    fact.append(fact[-1] * (i+1))

def main():
    n = int(input())
    r = input()
    b = input()
    cards = [0] * 3
    for i in range(n):
        if r[i]>b[i]:   cards[0] += 1
        elif r[i]<b[i]: cards[1] += 1
        else:           cards[2] += 1

    def dfs(cards):
        rest = sum(cards)
        if rest==0:
            return 1, 1
        f = fact[rest-1]
        nr, nb = 0, 0
        for i in range(3):
            if cards[i]==0: continue
            if i==0:
                nr += cards[i] * f
            elif i==1:
                nb += cards[i] * f
            else:
                cards_next = copy.copy(cards)
                cards_next[i] -= 1
                _nr, _nb = dfs(cards_next)
                nr += _nr * cards[i]
                nb += _nb * cards[i]
        return nr, nb
    nr, nb = dfs(cards)
    if nr>nb:   print("RED")
    elif nr<nb: print("BLUE")
    else:       print("EQUAL")
    # print(nr, nb)
    return

t = int(input())
for i in range(t):
    main()



# 誤読
# import copy

# MAXN = 1001
# fact = [1]
# for i in range(MAXN):
#     fact.append(fact[-1] * (i+1))

# def main():
#     n = int(input())
#     r = input()
#     b = input()
#     rcnt, bcnt = [0]*10, [0]*10
#     for i in range(n):
#         rcnt[int(r[i])] += 1
#         bcnt[int(b[i])] += 1

#     def dfs(rcnt, bcnt):
#         rest = sum(rcnt)
#         if rest==0:
#             return 1, 1
#         f = fact[rest-1]
#         nr, nb = 0, 0
#         for ri in range(10):
#             if rcnt[ri]==0: continue
#             for bi in range(10):
#                 if bcnt[bi]==0: continue
#                 if ri > bi:
#                     nr += rcnt[ri] * bcnt[bi] * f
#                 elif ri < bi:
#                     nb += rcnt[ri] * bcnt[bi] * f
#                 else:
#                     rcnt_next = copy.copy(rcnt)
#                     rcnt_next[ri] -= 1
#                     bcnt_next = copy.copy(bcnt)
#                     bcnt_next[bi] -= 1
#                     _nr, _nb = dfs(rcnt_next, bcnt_next)
#                     nr += _nr * rcnt[ri] * bcnt[bi]
#                     nb += _nb * rcnt[ri] * bcnt[bi]
#         return nr, nb
#     nr, nb = dfs(rcnt, bcnt)
#     if nr>nb:   print("RED")
#     elif nr<nb: print("BLUE")
#     else:       print("EQUAL")
#     print(nr, nb)
#     return

# t = int(input())
# for i in range(t):
#     main()
