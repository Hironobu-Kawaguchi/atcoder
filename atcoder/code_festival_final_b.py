# https://atcoder.jp/contests/code-festival-2014-final/tasks/code_festival_final_b

s = input()
ans = 0
for i, c in enumerate(s):
    if i%2:
        ans -= int(c)
    else:
        ans += int(c)
print(ans)
