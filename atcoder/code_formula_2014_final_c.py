# https://atcoder.jp/contests/code-formula-2014-final/tasks/code_formula_2014_final_c

S = input()
ans = set()
tmp = ''
flg = False
for c in S:
    if c=='@':
        if tmp:
            ans.add(tmp)
        tmp = ''
        flg = True
    elif c==' ':
        if tmp:
            ans.add(tmp)
        flg = False
    elif flg:
        tmp += c
if tmp:
    ans.add(tmp)
ans = sorted(list(ans))
for a in ans:
    print(a)
