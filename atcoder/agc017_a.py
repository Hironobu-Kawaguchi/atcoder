# https://atcoder.jp/contests/agc017/tasks/agc017_a

N, P = map(int, input().split())
A = list(map(int, input().split()))
odd, even = 0, 0
for i in range(N):
    if A[i] % 2:
        odd += 1
    else:
        even += 1
if odd == 0:
    if P:
        ans = 0
    else:
        ans = 2**N
else:
    ans = 2**(N-1)

print(int(ans))

# from math import factorial

# N, P = map(int, input().split())
# A = list(map(int, input().split()))
# odd, even = 0, 0
# for i in range(N):
#     if A[i] % 2:
#         odd += 1
#     else:
#         even += 1

# ans = 0
# for i in range(odd+1):
#     if i%2 == P:
#         ans += factorial(odd) / factorial(i) / factorial(odd-i)
# ans *= 2**even

# print(int(ans))



# N, P = map(int, input().split())
# A = list(map(int, input().split()))

# ans = 0
# for i in range(1<<N):
#     tmp = 0
#     for j in range(N):
#         if ((i>>j) & 1):
#             tmp += A[j]
#     if tmp%2 == P:
#         ans += 1

# print(ans)
