# D - Flipping Signs
# https://atcoder.jp/contests/abc125/tasks/abc125_d

N = int(input())
A = list(map(int, input().split()))
A.sort()

for i in range(N//2):
    if A[i*2] + A[i*2+1] < 0:
        A[i*2] = -1 * A[i*2]
        A[i*2+1] = -1 * A[i*2+1]
    else:
        break
# print(A)
print(sum(A))

"""
N = int(input())
A = list(map(int, input().split()))

num_of_minus = sum([a < 0 for a in A])
abs_A = [abs(a) for a in A]
ans = sum(abs_A)

if num_of_minus % 2 == 0:
    print(ans)
else:
    print(ans - 2 * min(abs_A))
"""

"""
jj = N-1
for i in range(N-1):
    if A[i] <= 0:
        j = jj
        while j > i+1:
            sumA = A[i] + A[j] - sum(A[i+1:j])
            if sumA < 0:
                A[i] = -1 * A[i]
                A[j] = -1 * A[j]
                # jj = j
                j = 0
            j -= 1

print(sum(A))
"""