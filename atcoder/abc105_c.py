# https://atcoder.jp/contests/abc105/tasks/abc105_c

N = int(input())

ans = ''
while N != 0:
    if N % 2 == 0:
        ans = '0' + ans
    else:
        N -= 1
        ans = '1' + ans
    N /= -2

if ans == '':
    print(0)
else:
    print(ans)
