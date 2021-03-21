# https://atcoder.jp/contests/agc006/tasks/agc006_a

N = int(input())
s = input()
t = input()

for i in range(N, -1, -1):
    if s[N-i:] == t[:i]:
        print(2*N-i)
        break
