# https://atcoder.jp/contests/agc011/tasks/agc011_b

N = int(input())
A = list(map(int, input().split()))
A.sort()
ans, suma = 1, 0
for i in range(N-1):
    suma += A[i]
    ans += 1
    if suma * 2 < A[i+1]:
        ans = 1
print(ans)


# N = int(input())
# A = list(map(int, input().split()))
# A.sort()
# cumA = [0]
# for i in range(N):
#     cumA.append(cumA[-1] + A[i])
# ans = 0
# if A[0] * 2 >= A[1]:
#     ans += 1
# for i in range(N-1):
#     if cumA[i+1] * 2 >= A[i+1]:
#         ans += 1
#     else:
#         ans = 1
# print(ans)
