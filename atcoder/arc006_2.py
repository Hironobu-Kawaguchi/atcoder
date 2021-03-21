# https://atcoder.jp/contests/arc006/tasks/arc006_2

N, L = map(int, input().split())
Amida = [input() for _ in range(L)]
start = input()
for i in range(N*2-1):
    if start[i] == 'o':
        now = i
        break

for r in range(L-1, -1, -1):
    if now != 0 and Amida[r][now-1] == '-':
        now -= 2
    elif now != N*2-2 and Amida[r][now+1] == '-':
        now += 2

print(now//2+1)
