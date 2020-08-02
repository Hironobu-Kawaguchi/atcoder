# https://atcoder.jp/contests/digitalarts2012/tasks/digitalarts_1

s = input().split()
# print(s)
N = int(input())
t = [input() for _ in range(N)]
# print(t)

def chk(s, t):
    n = len(s)
    if len(t) != n: return False
    for i in range(n):
        if s[i] != t[i] and t[i] != '*':
            return False
    return True

for i in range(len(s)):
    for j in range(N):
        if chk(s[i], t[j]):
            s[i] = '*' * len(s[i])
print(*s)
