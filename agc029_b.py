# B - Powers of two
# https://atcoder.jp/contests/agc029/tasks/agc029_b

N  =  int(input())
A  =  list(map(int, input().split()))
A.sort(reverse = True)
d  =  {}
cnt = 0

for a in A:
    if a not in d:
        d[a] = 1
    else:
        d[a] += 1
    
for i in range(N):
    if d[A[i]] == 0:
        continue
        
    d[A[i]] -= 1
    
    temp = 2 ** A[i].bit_length() - A[i]
    
    if temp in d and d[temp] > 0:
        cnt += 1
        d[temp]  -= 1
        
print(cnt)

"""
import math
N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

cnt = 0
i = 0
while i + cnt < N:
    temp = 2 ** int(math.log2(A[i]) + 1) - A[i]
    j = i + 1
    while j + cnt < N:
        if A[j] == temp:
            cnt += 1
            A.pop(j)
        j += 1
    i += 1

print(cnt)
"""