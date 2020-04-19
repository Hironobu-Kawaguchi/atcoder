# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9

def main(x):
    N = int(input())
    c = [0]*(24*60)
    j = [0]*(24*60)
    se = []
    min_i = 0
    for i in range(N):
        s, e = map(int, input().split())
        se.append((s,e,i))
        if s < se[min_i][0]:
            min_i = i
    se.sort()
    y = ['']*N
    for i in range(N):
        flg_c, flg_j = 0, 0
        for time in range(se[i][0], se[i][1]):
            if c[time] == 1:
                flg_c = 1
                break
        if flg_c == 0:
            y[se[i][2]] = 'C'
            for time in range(se[i][0], se[i][1]):
                c[time] = 1
        else:
            for time in range(se[i][0], se[i][1]):
                if j[time] == 1:
                    flg_j = 1
                    break
            if flg_j == 0:
                y[se[i][2]] = 'J'
                for time in range(se[i][0], se[i][1]):
                    j[time] = 1
            else:
                y = 'IMPOSSIBLE'
                print("Case #{}: {}".format(x, y))
                return
    print("Case #{}: {}".format(x, ''.join(y)))
    return

T = int(input())
for i in range(T):
    main(i+1)
