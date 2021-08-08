# https://atcoder.jp/contests/ABC213/tasks/abc213_c

H, W, N = map(int, input().split())
A, B = [], []
h_set, w_set = set(), set()
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    h_set.add(a)
    B.append(b)
    w_set.add(b)
h_d = dict(zip(sorted(list(h_set)), range(1, len(h_set)+1)))
# print(h_d)
w_d = dict(zip(sorted(list(w_set)), range(1, len(w_set)+1)))
# print(w_d)
for i in range(N):
    print(h_d[A[i]], w_d[B[i]])
