# B - Two Anagrams
# https://atcoder.jp/contests/abc082/tasks/abc082_b

s = input()
t = input()

ss = ''.join(sorted(s))
tt = ''.join(sorted(t, reverse=True))

if ss < tt:
    print('Yes')
else:
    print('No')
