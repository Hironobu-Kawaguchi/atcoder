# https://atcoder.jp/contests/abc053/tasks/abc053_b

s = input()
for i in range(len(s)):
    if s[i] == 'A':
        left = i
        break
for j in range(len(s) - 1, 0, -1):
    if s[j] == 'Z':
        right = j
        break
ans = len(s[left:right+1])
print(ans)
