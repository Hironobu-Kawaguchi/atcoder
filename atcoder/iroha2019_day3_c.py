# C - Not Say "NO"
# https://atcoder.jp/contests/iroha2019-day3/tasks/iroha2019_day3_c
# 1, 2 * (N-2) , 2+mod のプレゼントを割り当てる

N, K = map(int, input().split())
S = 'YES'

mod = K - (2 * N - 1)

if N == 1:
    V = list(range(1,K+1))
    R = [1] * K
elif N == 2:
    V = list(range(1,K))
    R = [1] * (K-1)
    sm = sum(V)
    V.append(sm)
    R.append(2)
else:
    V = list(range(10000,(2+mod)*10000+1, 10000))
    R = [1] * (2+mod)
    sm = sum(V)
    V.append(sm)
    R.append(2)
    for i in range(N-2):
        V += [sm//2+1+i, sm - (sm//2+1+i)]
        R += [i+3] * 2
print(*V)
print(S)
print(*R)
