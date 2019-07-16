"""
黒板に N 個の正の整数 A1,...,AN が書かれています．
すぬけ君は，黒板に書かれている整数がすべて偶数であるとき，次の操作を行うことができます．
黒板に書かれている整数すべてを，2 で割ったものに置き換える．
すぬけ君は最大で何回操作を行うことができるかを求めてください．
1≤N≤200
1≤Ai≤109
"""
"""
input();a=lambda x:0 if x%2 else 1+a(x//2);print(min(map(a,map(int,input().split()))))
"""
"""
N = int(input())
A = map(int, input().split())
print(min([(a & (-a)).bit_length() - 1 for a in A]))
"""
"""
n = int(input())
l = list(map(int, input().split()))
count = 0
 
while all(e % 2 == 0 for e in l):
    l = [e/2 for e in l]
    count += 1
 
print(count)
"""
n = int(input())
a = input().split()
#print(a)
cnt = 0
flg = 0
while flg == 0:
    for i,ai in enumerate(a):
        if int(ai) % 2 == 0:
            a[i] = int(ai) / 2
        else:
            flg = 1
    if flg == 0:
        cnt += 1
        #print(cnt)
print(cnt)
