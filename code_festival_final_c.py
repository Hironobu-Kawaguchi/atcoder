# https://atcoder.jp/contests/code-festival-2014-final/tasks/code_festival_final_c
# f(10000)=10**16

def f(x):
    s = str(x)
    n = len(s)
    res = 0
    for i in range(n):
        res += int(s[n-1-i]) * (x**i)
    return res

A = int(input())
for i in range(10, 10001):
    if f(i)==A:
        print(i)
        break
else:
    print(-1)
