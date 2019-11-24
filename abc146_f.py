# https://atcoder.jp/contests/abc146/tasks/abc146_f

N, M = map(int, input().split())
S = input()

ans = []
flg = 1
i = N
while i != 0:
    for j in range(min(M, i), 0, -1):
        if S[i-j] == '0':
            ans.append(j)
            i -= j
            break
    else:
        flg = -1
        i = 0
    # print(i)

if flg == -1:
    print(flg)
else:
    ans.reverse()
    print(*ans)
