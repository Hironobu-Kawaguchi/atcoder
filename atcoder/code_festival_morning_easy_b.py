# https://atcoder.jp/contests/code-festival-2014-morning-easy/tasks/code_festival_morning_easy_b

n = int(input())
div, mod = divmod(n-1,20)
if div%2==0:
    ans = mod+1
else:
    ans = 20-mod
print(ans)
