# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef2/00000000002d5b62

def solve():
    u = int(input())
    d = dict()
    for i in range(10000):
        q = input()
        if q[:2] == '-1': continue
        q, r = q.split()
        n = len(r)
        if len(q)==n:
            flg = True
        else:
            flg = False
        for j in range(n):
            if flg:
                q_num = int(q[j])
                if r[j] not in d:
                    d[r[j]] = q_num
                elif d[r[j]] > q_num:
                    d[r[j]] = q_num
                if (j==0 and q_num>1) or q_num==0:
                    flg = False
            else:
                if r[j] not in d:
                    d[r[j]] = 9
    ds = []
    for k in d:
        ds.append([d[k], k])
    ds.sort()
    ret = ''
    for v, k in ds:
        ret += k

    return ret

T = int(input())
for x in range(T):
    y = solve()
    print('Case #{}:'.format(x + 1), y)
