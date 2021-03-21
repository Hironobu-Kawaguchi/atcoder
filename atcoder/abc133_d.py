# 
N = int(input())
A = list(map(int, input().split()))

B = []
b = 0
for i in range(N):
    if i % 2 == 0:
        b += A[i]
    else:
        b -= A[i]
B.append(b)
for i in range(1, N):
    b *= -1
    b += A[i-1] * 2
    B.append(b)

print(*B)
