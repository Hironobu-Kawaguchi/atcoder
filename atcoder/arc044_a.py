# https://atcoder.jp/contests/arc044/tasks/arc044_a

N = int(input())

if N == 1:
    print("Not Prime")
elif N in [2, 3, 5] or (N%5 and N%2 and N%3):
    print("Prime")
else:
    print("Not Prime")
