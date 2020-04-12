# https://atcoder.jp/contests/abc162/tasks/abc162_a

N = input()
flg = False
for i in range(len(N)):
    if N[i] == '7':
        flg = True
        break
if flg:
    print('Yes')
else:
    print('No')


# S = input()
# X, Y, Z = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
