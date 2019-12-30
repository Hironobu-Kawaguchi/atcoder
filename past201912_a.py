# https://atcoder.jp/contests/past201912/tasks/past201912_a

from string import ascii_lowercase
S = input()
flg = True
for s in S:
    if s in ascii_lowercase:
        flg = False
if flg:
    print(int(S)*2)
else:
    print("error")
