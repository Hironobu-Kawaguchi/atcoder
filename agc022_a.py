# https://atcoder.jp/contests/agc022/tasks/agc022_a

from string import ascii_lowercase
D = {k:i for i, k in enumerate(ascii_lowercase)}

S = input()
n = len(S)

if n != 26:
    ans = S
    for c in ascii_lowercase:
        if c not in S:
            ans += c
            break
else:
    nokori = [D[S[-1]]]
    for i in range(24, -1, -1):
        res = 30
        for n in nokori:
            if D[S[i]] < n:
                res = min(res, n)
        if res == 30:
            nokori.append(D[S[i]])
        else:
            ans = S[:i] + ascii_lowercase[res]
            break
    else:
        ans = -1

print(ans)
