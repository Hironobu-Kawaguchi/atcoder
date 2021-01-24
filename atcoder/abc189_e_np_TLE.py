# https://atcoder.jp/contests/abc189/tasks/abc189_e
# アフィン変換
import numpy as np
import sys
input = sys.stdin.readline

N = int(input())
# xy = np.ones((N,3), dtype=int)
# for i in range(N):
#     xy[i,:2] = np.array(list(map(int, input().split())))
xy = [np.array(list(map(int, input().split())) + [1], dtype=np.int64).T for i in range(N)]
M = int(input())
# A = np.zeros((M+1, 3,3), dtype=np.int64)
A = [0] * (M+1)
A[0] = np.eye(3, dtype=np.int64)
# print(A[0])
for i in range(M):
    op = input()
    if op[0] == '1':
        x = np.array([[ 0, 1, 0],[-1, 0, 0],[ 0, 0, 1]])
    elif op[0] == '2':
        x = np.array([[ 0,-1, 0],[ 1, 0, 0],[ 0, 0, 1]])
    else:
        o, p = map(int, op.split())
        if o==3:
            x = np.array([[-1, 0,2*p],[ 0, 1, 0],[ 0, 0, 1]])
        elif o==4:
            x = np.array([[ 1, 0, 0],[ 0,-1,2*p],[ 0, 0, 1]])
    A[i+1] = np.dot(x, A[i])
    # print(A[i+1])
Q = int(input())
for i in range(Q):
    a, b = map(int, input().split())
    ans = np.dot(A[a], xy[b-1])
    print(ans[0], ans[1])
