# https://atcoder.jp/contests/abc154/tasks/abc154_a

S, T = input().split()
A, B = map(int, input().split())
U = input()

if U == S:
    A -= 1
elif U == T:
    B -= 1
print(A, B)
