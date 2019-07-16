# D - XOR World
# https://atcoder.jp/contests/abc121/tasks/abc121_d
# f(A,B) を A,A+1,...,B の排他的論理和としたとき、f(A,B) を求めてください。
# 排他的論理和とは
# 整数 c1,c2,...,cn のビットごとの排他的論理和 y は、以下のように定義されます。
# y を二進表記した際の 2k (k≥0) の位の数は、c1,c2,...,cn のうち、二進表記した際の 2k の位の数が 1 となるものが奇数個ならば 1、偶数個ならば 0である。
# 例えば、3 と 5 の排他的論理和は 6 です(二進数表記すると: 011 と 101 の排他的論理和は 110 です)。

# f(A,B)=f(0,A-1)^f(0,B) ∵ n^n=0
# 偶数nについて、n^(n+1)=1 0^1=1,0^1^2^3=0,

A, B = map(int, input().split())
def xorchk(n):
    if n%4 == 0:
        return n
    elif n%4 == 1:
        return 1
    elif n%4 == 2:
        return n+1
    else:
        return 0
print(xorchk(A-1)^xorchk(B))
"""
import math
A, B = map(int, input().split())
l = []
keta = int(math.log2(B)) + 1
fmt = '0' + str(keta) + 'b'
# print(keta)
for i in range(A, B+1):
    l.append(format(i, fmt))
    # print(i, l[i-A])
bbin = ['0'] * keta
for j in range(keta):
    for i in range(A, B+1):
        if l[i-A][j] == '1':
            if bbin[j] == '0':
                bbin[j] = '1'
            else:
                bbin[j] = '0'
# print(bbin)
print(int("".join(bbin), 2))
"""