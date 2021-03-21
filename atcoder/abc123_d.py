# D - Cake 123
# https://atcoder.jp/contests/abc123/tasks/abc123_d
import heapq
X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
B = list(map(int, input().split()))
B.sort(reverse=True)
C = list(map(int, input().split()))
C.sort(reverse=True)
q = [(-(A[0] + B[0] + C[0]), 0, 0, 0)]
s = set()
for n in range(K):
    p, a, b, c = heapq.heappop(q)
    print(-p)
    if a+1 < X and ((a+1, b, c) not in s):
        s.add((a+1, b, c))
        heapq.heappush(q, (-(A[a+1] + B[b] + C[c]), a+1, b, c))
    if b+1 < Y and ((a, b+1, c) not in s):
        s.add((a, b+1, c))
        heapq.heappush(q, (-(A[a] + B[b+1] + C[c]), a, b+1, c))
    if c+1 < Z and ((a, b, c+1) not in s):
        s.add((a, b, c+1))
        heapq.heappush(q, (-(A[a] + B[b] + C[c+1]), a, b, c+1))
"""
X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
B = list(map(int, input().split()))
B.sort(reverse=True)
C = list(map(int, input().split()))
C.sort(reverse=True)

ABC = []
for xi in range(X):
    if xi+1 > K:
        break
    for yi in range(Y):
        if (xi+1)*(yi+1) > K:
            break
        for zi in range(Z):
            if (xi+1)*(yi+1)*(zi+1) > K:
                break
            ABC.append(A[xi]+B[yi]+C[zi])
ABC.sort(reverse=True)
for i in range(K):
    print(ABC[i])      
"""