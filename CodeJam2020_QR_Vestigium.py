# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020993c

def main(x):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    k, r, c = 0, 0, 0
    for i in range(N):
        k += M[i][i]
        rows = [0]*N
        for j in range(N):
            rows[M[i][j]-1] += 1
        for j in range(N):
            if rows[j] != 1:
                r += 1
                break
        cols = [0]*N
        for j in range(N):
            cols[M[j][i]-1] += 1
        for j in range(N):
            if cols[j] != 1:
                c += 1
                break
    print("Case #{}: {} {} {}".format(x, k, r, c))

T = int(input())
for i in range(T):
    main(i+1)
