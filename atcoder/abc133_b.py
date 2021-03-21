# 
import math
N, D = map(int, input().split())

l = []

for i in range(N):
    l.append(list(map(int, input().split())))

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        sumx = 0
        for k in range(D):
            sumx += (l[i][k] - l[j][k]) ** 2
        sum_sqrt = math.sqrt(sumx)
        if sum_sqrt.is_integer():
            ans += 1

print(ans)
