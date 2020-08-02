# https://atcoder.jp/contests/abc039/tasks/abc039_d

H, W = map(int, input().split())
S = [input() for _ in range(H)]
dk = [-1, 0, 1]

T = []
for i in range(-1, H+1):
    t = ''
    for j in range(-1, W+1):
        nt = '#'
        for dx in range(3):
            ni = i + dk[dx]
            if (ni<0 or ni>=H): continue
            for dy in range(3):
                nj = j + dk[dy]
                if (nj<0 or nj>=W): continue
                if S[ni][nj] == '.':
                    nt = '.'
        t += nt
    T.append(t)
# print(T)

SS = []
for i in range(1, H+1):
    ss = ''
    for j in range(1, W+1):
        nss = '.'
        for dx in range(3):
            ni = i + dk[dx]
            if (ni<1 or ni>=H+1): continue
            for dy in range(3):
                nj = j + dk[dy]
                if (nj<1 or nj>=W+1): continue
                if T[ni][nj] == '#':
                    nss = '#'
        ss += nss
    SS.append(ss)
# print(SS)

if S == SS:
    print('possible')
    for i in range(1, H+1):
        print(T[i][1:-1])
else:
    print('impossible')
