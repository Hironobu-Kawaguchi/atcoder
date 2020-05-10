# https://atcoder.jp/contests/code-formula-2014-quala/tasks/code_formula_2014_qualA_b

a, b = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

ans = ['x'] * 10
for i in range(a):
    ans[p[i]] = '.'
for i in range(b):
    ans[q[i]] = 'o'

ans.append(ans[0])
print(*ans[7:])
print('',*ans[4:7])
print(' ',*ans[2:4])
print('  ',ans[1])
