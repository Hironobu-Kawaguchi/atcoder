# https://atcoder.jp/contests/abc101/tasks/abc101_b

N = input()
sn = 0
for i in range(len(N)):
    sn += int(N[i])

if int(N) % sn:
    ans = 'No'
else:
    ans = 'Yes'

print(ans)
