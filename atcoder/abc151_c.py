# https://atcoder.jp/contests/abc151/tasks/abc151_c

N, M = map(int, input().split())

acs = [0] * N
was = [0] * N 

for i in range(M):
    p, s = input().split()
    j = int(p) - 1
    if s == 'AC':
        acs[j] = 1
    elif s == 'WA':
        if acs[j] == 0:
            was[j] += 1

ac, wa = 0, 0
for i in range(N):
    ac += acs[i]
    if acs[i]:
        wa += was[i]

print(ac, wa)
