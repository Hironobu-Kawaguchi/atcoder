# https://atcoder.jp/contests/abc087/tasks/abc087_b

A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            tmp = 500 * a + 100 * b + 50 * c
            if tmp == X:
                ans += 1
print(ans)



# ans = 0
# for a in range(min(A+1, X//500 + 1)):
#     for b in range(min(B+1, (X - 500*a)//100 + 1)):
#         tmp = X - 500 * a - 100 * b
#         if tmp % 50 == 0 and tmp >= 0 and tmp <= 50 * C:
#             ans += 1

# print(ans)
