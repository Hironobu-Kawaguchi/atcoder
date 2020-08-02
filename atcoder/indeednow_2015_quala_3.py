# https://atcoder.jp/contests/indeednow-quala/tasks/indeednow_2015_quala_3

N = int(input())
s = [int(input()) for _ in range(N)]
s.sort(reverse=True)
Q = int(input())
for i in range(Q):
    k = int(input())
    if k > N-1 or s[k] == 0:
        ans = 0
    else:
        ans = s[k] + 1
    print(ans)
