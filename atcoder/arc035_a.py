# https://atcoder.jp/contests/arc035/tasks/arc035_a

s = input()
ans = "YES"
for i in range(len(s)//2):
    if s[i] == '*' or s[-i-1] == '*' or s[i] == s[-1-1]:
        continue
    else:
        ans = "NO"
        break
print(ans)
