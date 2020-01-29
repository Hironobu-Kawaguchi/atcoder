# https://atcoder.jp/contests/code-festival-2016-quala/tasks/codefestival_2016_qualA_c

s = input()
K = int(input())

ans = ''
for i, c in enumerate(s):
    dif = ord('z') - ord(c) + 1
    dif %= 26
    if i == len(s) - 1:
        K %= 26
        if ord(c) + K > ord('z'):
            K -= 26
        ans += chr(ord(c) + K)
    elif dif <= K:
        ans += 'a'
        K -= dif
    else:
        ans += c
print(ans)
