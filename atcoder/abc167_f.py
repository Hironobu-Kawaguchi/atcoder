# https://atcoder.jp/contests/abc167/tasks/abc167_f

import sys
def input(): return sys.stdin.readline().rstrip()

n = int(input())
ls, rs = [], []
total = 0
for i in range(n):
    s = input()
    h, b = 0, 0
    for c in s:
        if c=='(':  h += 1
        else:       h -= 1
        b = min(b, h)
    if h > 0:   ls.append((b, h))       # 増減+ はb:最下点, h:増減を取る
    else:       rs.append((b-h, -h))    # 増減- は、上下左右逆さに考え、b:右から見た最下点、h:増減のマイナスを取る
    total += h
ls.sort(reverse=True)
rs.sort(reverse=True)   # 増減-は右から見るので、大きい順にsort

def chk(s):
    h = 0
    for sb, sh in s:
        b = h + sb
        if b < 0: return False
        h += sh
    return True

if (chk(ls) and chk(rs) and total==0):
    print("Yes")
else:
    print("No")


# WA
# import sys
# def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.buffer.readline

# N = int(input())
# tbl = []
# sum_left, sum_right, sum_maxdif, sum_dif = 0, 0, 0, 0
# for i in range(N):
#     S = input()
#     left = 0
#     right = 0
#     maxdif = 0
#     for c in S:
#         if c=='(':
#             left += 1
#         else:
#             right += 1
#         maxdif = max(maxdif, right - left)
#     if S[0] == '(':
#         s = True
#     else:
#         s = False
#     if S[-1] == ')':
#         e = True
#     else:
#         e = False
#     tbl.append([left-right, left, right, maxdif, s, e])
#     sum_left += left
#     sum_right += right
#     sum_maxdif += maxdif
#     sum_dif += max(left-right, 0)
# tbl.sort()
# for i in range(N):
#     if tbl[i][5]:
#         if tbl[i][0] > 0:
#             sum_dif -= tbl[i][0]
#         break
# for i in range(N-1, -1, -1):
#     if tbl[i][4]:
#         if tbl[i][3] < 0:
#             sum_dif -= tbl[i][0]
#         break
    
# if sum_left != sum_right:
#     print('No')
# elif sum_maxdif > sum_dif:
#     print('No')
# else:
#     print('Yes')
