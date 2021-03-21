# https://atcoder.jp/contests/agc003/tasks/agc003_a

S = input()
d = {'N': 0, 'S': 0, 'W': 0, 'E': 0}
for s in S:
    d[s] = 1

ans = "Yes"
if (d['N'] ^ d['S']) or (d['W'] ^ d['E']):
    ans = "No"

print(ans)
