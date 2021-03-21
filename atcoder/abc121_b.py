"""
B - Can you solve this?
https://atcoder.jp/contests/abc121/tasks/abc121_b
N  個のソースコードがあり、i 個目のソースコードの特徴は Ai1,Ai2,...,AiM の M 個の整数で表されます。
また、整数 B1,B2,...,BM と 整数 C が与えられます。
Ai1B1+Ai2B2+...+AiMBM+C>0 のときに限り、i 個目のソースコードはこの問題に正答するソースコードです。
N 個のソースコードのうち、この問題に正答するソースコードの個数を求めてください。
"""
"""
N,M,C = map(int,input().split())
B = [int(i) for i in input().split()]
A = [[int(i) for i in input().split()] for _ in range(N)]
count = 0
for i in range(N):
    if(sum(j[0]*j[1] for j in zip(A[i],B))+C>0):
        count = count + 1
print(count)
"""
import numpy as np
N, M, C = map(int, input().split())
B = np.array(list(map(int, input().split())))
A = np.empty((N, M),dtype=int)
for n in range(N):
    A[n, :] = list(map(int, input().split()))
X = np.dot(A, B) + C
print(len(X[X>0]))