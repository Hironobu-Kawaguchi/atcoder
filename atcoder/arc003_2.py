# https://atcoder.jp/contests/arc003/tasks/arc003_2

N = int(input())
s = [input() for _ in range(N)]
s_reversed = []
for i in range(N):
    s_reversed.append(s[i][::-1])
s_reversed.sort()
for i in range(N):
    print(s_reversed[i][::-1])
