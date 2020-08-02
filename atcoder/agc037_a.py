# https://atcoder.jp/contests/agc037/tasks/agc037_a

S = input()
n = len(S)
K = 1
i = 1
while i < n:
    if S[i-1] == S[i]:
        if i == n - 1:
            i += 1
        elif i == n - 2:
            i += 2
            K += 1
        else:
            i += 3
            K += 2
    else:
        i += 1
        K += 1

print(K)
