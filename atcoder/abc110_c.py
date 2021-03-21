# https://atcoder.jp/contests/abc110/tasks/abc110_c

S = input()
T = input()

def str2num(s):
    d = {}
    ret = []
    idx = 0
    for ch in s:
        if ch not in d:
            d[ch] = idx
            idx += 1
        ret.append(d[ch])
    return ret

if str2num(S) == str2num(T):
    print('Yes')
else:
    print('No')
    