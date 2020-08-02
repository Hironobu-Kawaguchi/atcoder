# https://atcoder.jp/contests/agc016/tasks/agc016_a

from string import ascii_lowercase
D = {k:i for i, k in enumerate(ascii_lowercase)}

s = input()
n = len(s)
lst = [[] for _ in range(26)]

for i in range(n):
    lst[D[s[i]]].append(i)
# print(lst)

ans = n//2
for i in range(26):
    nums = lst[i]
    if len(nums) > 0:
        tmp = lst[i][0]
        for j in range(len(nums)-1):
            tmp = max(tmp, lst[i][j+1] - lst[i][j] - 1)
        tmp = max(tmp, n - lst[i][-1] - 1)
        ans = min(ans, tmp)

print(ans)
