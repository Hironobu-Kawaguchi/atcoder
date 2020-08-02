# https://atcoder.jp/contests/arc006/tasks/arc006_1

E = set(map(int, input().split()))
B = int(input())
L = list(map(int, input().split()))

match = 0
bonus = 0
for i in range(6):
    if L[i] in E:
        match += 1
    elif L[i] == B:
        bonus = 1

if match == 6:
    ans = 1
elif match == 5 and bonus:
    ans = 2
elif match >= 3:
    ans = 8 - match
else:
    ans = 0

print(ans)
