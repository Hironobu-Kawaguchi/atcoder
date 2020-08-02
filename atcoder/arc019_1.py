# https://atcoder.jp/contests/arc019/tasks/arc019_1

d = {'O': '0', 'D': '0', 'I': '1', 'Z': '2', 'S': '5', 'B': '8'}
S = input()
ans = ''
for s in S:
    if s in d:
        ans += d[s]
    else:
        ans += s
print(ans)
