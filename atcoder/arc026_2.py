# https://atcoder.jp/contests/arc026/tasks/arc026_2
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

N = int(input())
sumd = 0
i = 1
while i*i<=N:
    if N%i==0:
        sumd += i
        if i*i!=N:
            sumd += N//i
    i += 1
if sumd > 2*N:
    print("Abundant")
elif sumd == 2*N:
    print("Perfect")
else:
    print("Deficient")
