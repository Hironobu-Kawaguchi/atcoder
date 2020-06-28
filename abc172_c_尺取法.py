# https://atcoder.jp/contests/abc172/tasks/abc172_c
import sys
input = sys.stdin.buffer.readline

N, M, K = map(int, input().split())
A = list(map(int, (input().split())))
B = list(map(int, (input().split())))
t = sum(B)
# 尺取法
j = M   # bはmから減らしていく
ans = 0
for i in range(N+1):    # aは0からnまで増やしていく
    if i: t += A[i-1]   # i個までの累計になるように足す 0個は0
    while (j>0 and t>K):    # t<=k または j==0 で抜ける
        j -= 1
        t -= B[j]
    if t>K: break   # bが0番まで行っても　t>k の場合はだめ
    ans = max(ans, i+j)
print(ans)
