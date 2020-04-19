import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def solve():
    H, W = map(int, readline().split())
    S = []
    for _ in range(H):
        S += list(map(int, readline().split()))
    N = (H * W)
    L = [-1] * (N + 1)
    R = [-1] * (N + 1)
    D = [-1] * (N + 1)
    U = [-1] * (N + 1)
    for n in range(N):
        h, w = divmod(n, W)
        if w != 0:
            L[n] = n - 1
        if w != W - 1:
            R[n] = n + 1
        if h != 0:
            D[n] = n - W
        if h != H - 1:
            U[n] = n + W

    full = sum(S)
    ret = full
    cand = list(range(N))  # 次に消す候補
    while cand:
        eliminate = []
        for v in cand:
            me = S[v]
            if me == 0:
                continue
            x = 0
            for i in (L[v], R[v], D[v], U[v]):
                if i != -1:
                    x += S[i] - me
            if x > 0:
                eliminate.append(v)
        if not eliminate:
            break
        cand = []
        for v in eliminate:
            full -= S[v]
            S[v] = 0
            if R[v] != -1:
                L[R[v]] = L[v]
            if L[v] != -1:
                R[L[v]] = R[v]
            if U[v] != -1:
                D[U[v]] = D[v]
            if D[v] != -1:
                U[D[v]] = U[v]
            cand += [L[v], R[v], D[v], U[v]]
        cand = set(cand)
        cand.discard(-1)
        ret += full
    return ret


T = int(readline())
for t in range(T):
    n = solve()
    print('Case #{}:'.format(t + 1), n)
