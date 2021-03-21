# https://atcoder.jp/contests/arc009/tasks/arc009_2

b = list(map(int, input().split()))
bb = [0] * 10
for i in range(10):
    bb[b[i]] = i
N = int(input())
a = ['{:09}'.format(int(input())) for _ in range(N)]
# print(a)

chglst = []
for i in range(N):
    tmp = ''
    for s in a[i]:
        tmp += str(bb[int(s)])
    chglst.append(tmp)
chglst.sort()
# print(chglst)

for i in range(N):
    tmp = ''
    for s in chglst[i]:
        tmp += str(b[int(s)])
    print(int(tmp))
