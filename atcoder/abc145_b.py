# https://atcoder.jp/contests/abc145/tasks/abc145_b

N = int(input())
S = input()

if S[:N//2] == S[N//2:]:
    print("Yes")
else:
    print("No")
