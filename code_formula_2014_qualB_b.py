# https://atcoder.jp/contests/code-formula-2014-qualb/tasks/code_formula_2014_qualB_b

N = input()
a = 0
b = 0
cnt = 0
for i, c in enumerate(N):
    cnt += 1
    if i%2:
        a += int(c)
    else:
        b += int(c)
if cnt%2:
    print(a,b)
else:
    print(b,a)
