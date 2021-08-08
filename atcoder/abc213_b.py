# https://atcoder.jp/contests/ABC213/tasks/abc213_b

N = int(input())
A = list(map(int, (input().split())))
B = [(a, i+1) for i, a in enumerate(A)]
B.sort()
print(B[-2][1])
