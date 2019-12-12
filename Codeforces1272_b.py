# https://codeforces.com/contest/1272/problem/B

from collections import Counter
def main():
    S = input()
    c = Counter(S)
    LR = min(c['L'], c['R'])
    UD = min(c['U'], c['D'])
    if LR == 0 and UD == 0:
        ans = ''
    elif LR == 0:
        ans = 'UD'
    elif UD == 0:
        ans = 'LR'
    else:
        ans = 'L' * LR + 'U' * UD + 'R' * LR + 'D' * UD
    print(len(ans))
    print(ans)

q = int(input())
for i in range(q):
    main()
