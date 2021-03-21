# https://codeforces.com/contest/1326/problem/D

def chk(s):
    """ 回文チェック """
    n = len(s) // 2
    for i in range(n):
        if s[i] != s[-1-i]:
            return False
    return True

def left(s):
    n = len(s)
    for i in range(n-1,0,-1):
        if chk(s[:i]):
            return s[:i]

def right(s):
    n = len(s)
    for i in range(1,n):
        if chk(s[i:]):
            return s[i:]

def chk2(s):
    l = left(s)
    r = right(s)
    if len(l) >= len(r):
        return l
    else:
        return r

def chk1(s):
    i = 0
    while s[i] == s[-1-i]:
        i += 1
    res = s[:i] + chk2(s[i:-i]) + s[-i:]
    return res

def main(s):
    if chk(s):
        return s
    if s[0] == s[-1]:
        res = chk1(s)
    else:
        res = chk2(s)
    return res

t = int(input())
for i in range(t):
    s = list(input())
    print(''.join(main(s)))
