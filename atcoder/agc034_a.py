# A - Kenken Race
# https://atcoder.jp/contests/agc034/tasks/agc034_a
# C < D の場合、A-Dに#2連続なし
# C > D の場合、A-Cに#2連続なし かつ B+1 - D+1に.3連続あり
# C < B の場合、A-Cに#2連続なし かつ B-Dに#2連続なし なので C-Bに#2連続があっても良い

N, A, B, C, D = map(int,input().split())
S = input()

pres = 'x'          # S[i-1]
cntx, cnty = 0, 0   # x:'.'の連続数, y:'#'の連続数
mxx, mxy = 1, 1     # mxx:'.'の連続数max, mxy:'#'の連続数max

for i in range(A-1, max(C, D)): # base=0
    if S[i] == pres:
        if S[i] == '.':
            cntx += 1
            if i >= B and i < D+1:  # .のチェックは B+1 - D+1だけ
                mxx = max(cntx, mxx)
        elif S[i] == '#':
            cnty += 1
            if C > B or (i < C and i >= B-1):   # C < B の場合は、C-Bでは#の数は不問
                mxy = max(cnty, mxy)
    else:
        pres = S[i]
        if S[i] == '.':
            cntx = 1
        elif S[i] == '#':
            cnty = 1

if C < D:
    if mxy < 2:
        print("Yes")
    else:
        print("No")
else:
    if mxy < 2 and mxx >= 3:
        print("Yes")
    else:
        print("No")
