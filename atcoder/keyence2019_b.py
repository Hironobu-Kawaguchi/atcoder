# https://atcoder.jp/contests/keyence2019/tasks/keyence2019_b

S = input()
k = 'keyence'
n = len(S) - len(k)

ans = 'NO'
for i in range(len(S)-n):
    tmp = S[:i] + S[i+n:]
    if tmp == k:
        ans = 'YES'
        break

print(ans)
