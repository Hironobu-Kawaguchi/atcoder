# https://atcoder.jp/contests/abc066/tasks/abc066_b

S = input()
N = len(S)

for i in range(N-2, 1, -2):
    if S[:i//2] == S[i//2: i]:
        print(i)
        break
