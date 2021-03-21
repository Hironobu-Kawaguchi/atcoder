import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
import string
import re

A_to_Z = ''.join(string.ascii_uppercase)


def test(pattern, S):
    p = pattern.replace('*', '.*')
    if re.fullmatch(p, S):
        return True
    return False


def solve(words):
    prefix = []
    suffix = []
    mid = []
    full = []
    for w in words:
        w_spl = w.split('*')
        prefix.append(w_spl[0])
        suffix.append(w_spl[-1])
        if len(w_spl) == 1:
            full.append(w)
        for ww in w_spl[1:-1]:
            mid.append(ww)
    if full:
        S = max(full, key=len)
        if all(test(w, S) for w in words):
            return S
        else:
            return '*'
    P = max(prefix, key=len)
    S = max(suffix, key=len)
    if not all(P.startswith(p) for p in prefix):
        return '*'
    if not all(S.endswith(s) for s in suffix):
        return '*'
    T = P + ''.join(mid) + S
    return T


T = int(readline())
for t in range(1, T + 1):
    N = int(readline())
    words = tuple(readline().rstrip().decode() for _ in range(N))
    w = solve(words)
    print('Case #{}:'.format(t), w)
