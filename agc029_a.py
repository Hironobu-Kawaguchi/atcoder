# A - Irreversible operation
# https://atcoder.jp/contests/agc029/tasks/agc029_a

S = input()
cnt = 0
ans = 0
left = 0
for i in range(len(S)):
    if S[i] == 'W':
        cnt += S[left:i].count('B')
        ans += cnt
        left = i
print(ans)
