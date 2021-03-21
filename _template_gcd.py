# Template for AtCoder

#最大公約数、最小公倍数
import fractions
a,b=map(int, input().split())
f=fractions.gcd(a,b)
f2=a*b//f
print(f,f2)
