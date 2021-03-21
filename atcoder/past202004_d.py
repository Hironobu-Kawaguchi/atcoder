# https://atcoder.jp/contests/past202004-open/tasks/past202004_d

from itertools import product
from string import ascii_lowercase
chars = ascii_lowercase + '.'


def check(t, s):
    n = len(t)
    for i in range(len(s)-n+1):
        res = True
        for j in range(n):
            if t[j]!=s[i+j] and t[j]!='.':
                res = False
        if res:
            return res
    return False

def main():
    s = input()
    ans = 0
    for i in range(1,4):
        if i>len(s): continue
        for t in product(chars, repeat=i):
            # print(t)
            if check(t,s):
                ans += 1
                # print(t)
    print(ans)

main()
