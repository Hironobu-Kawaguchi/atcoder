# C - AB Substrings
# https://atcoder.jp/contests/diverta2019/tasks/diverta2019_c

N = int(input())
cntA, cntB, cntBoth, ans = 0, 0, 0, 0

for i in range(N):
    s = input()
    L = len(s)
    if s[0] == 'B':
        cntB += 1
    if s[L-1] == 'A':
        cntA += 1
    if s[0] == 'B' and s[L-1] == 'A':
        cntBoth += 1
    for i in range(L-1):
        if s[i:i+2] == 'AB':
            ans += 1
# print(ans, cntA, cntB, cntBoth)
ans += min(cntA, cntB)
if cntA == cntB and cntA == cntBoth and cntBoth > 0:
    ans -= 1
print(ans)
