# https://atcoder.jp/contests/past201912/tasks/past201912_h

N = int(input())
C = list(map(int, input().split()))
Q = int(input())
sm, mineven, minodd = 0, 10**9, 10**9
for i in range(N):
    sm += C[i]
    if i%2:
        mineven = min(mineven, C[i])
    else:
        minodd = min(minodd, C[i])

minuseven, minusodd = 0, 0
for i in range(Q):
    S = list(input().split())
    if S[0] == '1':
        x = int(S[1]) - 1
        a = int(S[2])
        if x%2:
            minus = minuseven
        else:
            minus = minusodd
        if C[x] - minus >= a:
            C[x] -= a
            if x%2:
                mineven = min(mineven, C[x])
            else:
                minodd = min(minodd, C[x])
    elif S[0] == '2':
        a = int(S[1])
        if minodd - minusodd >= a:
            minusodd += a
    else:
        a = int(S[1])
        if min(mineven - minuseven, minodd - minusodd) >= a:
            minuseven += a
            minusodd += a
    # print(i, C, minuseven, minusodd)

# print(sm, C, minuseven, minusodd)
print(sm - sum(C) + minuseven*(N//2) + minusodd*((N+1)//2))
