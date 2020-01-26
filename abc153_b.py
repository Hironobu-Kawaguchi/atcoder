# https://atcoder.jp/contests/abc153/tasks/abc153_b

H, N = map(int, input().split())
A = list(map(int, input().split()))
if H <= sum(A):
    print("Yes")
else:
    print("No")
