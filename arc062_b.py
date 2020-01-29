# https://atcoder.jp/contests/arc062/tasks/arc062_b

s = input()
ans = len(s)//2 - sum(c=='p' for c in s)
print(ans)
