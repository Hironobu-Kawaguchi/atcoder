# https://atcoder.jp/contests/arc081/tasks/arc081_b

MOD = 10**9+7
N = int(input())
S = input()
S2 = input()
lst = []
i = 0
while i < N:
    if i == N-1 or S[i] != S[i+1]:
        lst.append(1)
        i += 1
    else:
        lst.append(2)
        i += 2
if lst[0] == 1:
    ans = 3
else:
    ans = 6
for j in range(1, len(lst)):
    if lst[j-1] == 1:
        ans *= 2
    elif lst[j-1] == 2 and lst[j] == 2:
        ans *= 3
    ans %= MOD
print(ans)
