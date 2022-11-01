# https://atcoder.jp/contests/abc218/tasks/abc218_c

N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]
# print(S)
# print(T)

def round90(grid):
    new_grid = [['']*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # print(i,j, new_grid)
            new_grid[j][N-i-1] = grid[i][j]
    return new_grid

def slide(grid):
    for i in range(N):
        for j in range(N):
            if grid[i][j]=='#':
                si = i
                break
        if grid[i][j]=='#':
            break
    for j in range(N):
        for i in range(N):
            if grid[i][j]=='#':
                sj = j
                break
        if grid[i][j]=='#':
            break
    # print(si, sj)
    new_grid = [['']*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # print(i,j,si,sj,(i+si)%N,(j+sj)%N, new_grid)
            new_grid[i][j] = grid[(i+si)%N][(j+sj)%N]
    return new_grid

ans = "No"
S = slide(S)
for r in range(4):
    # print(S)
    # print(slide(T))
    if S==slide(T):
        ans = "Yes"
        break
    T = round90(T)
print(ans)

