# https://atcoder.jp/contests/abc295/tasks/abc295_b

def main():
    R, C = map(int, input().split())
    B = [list(input()) for _ in range(R)]
    # print(B)
    for i in range(R):
        for j in range(C):
            if B[i][j]!='.' and B[i][j]!='#':
                num = int(B[i][j])
                for ii in range(R):
                    for jj in range(C):
                        if B[ii][jj]!='.' and B[ii][jj]!='#': continue
                        if abs(i-ii) + abs(j-jj) <= num:
                            B[ii][jj] = '.'
    # for i in range(R):
    #     print(''.join(B[i]))
    for i in range(R):
        for j in range(C):
            if B[i][j]!='.' and B[i][j]!='#':
                B[i][j] = '.'
    for i in range(R):
        print(''.join(B[i]))
    return

main()
