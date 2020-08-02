# B - YYMM or MMYY
# https://atcoder.jp/contests/abc126/tasks/abc126_b

# S = input()

# s12 = int(S[:2])
# s34 = int(S[3:])
# dic_mmdd = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

S = int(input())
s12 = S // 100
s34 = S % 100

if s34 >=1 and s34 <= 12:
    yymm = True
else:
    yymm = False

if s12 >=1 and s12 <= 12:
    mmyy = True
else:
    mmyy = False

if yymm and mmyy:
    ans = 'AMBIGUOUS'
elif yymm:
    ans = 'YYMM'
elif mmyy:
    ans = 'MMYY'
else:
    ans = 'NA'

print(ans)
