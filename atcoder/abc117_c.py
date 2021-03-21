# C - Streamline
# https://atcoder.jp/contests/abc117/tasks/abc117_c

N, M  = map(int, input().split())
X = list(map(int, input().split()))
X.sort()
xd = [X[i+1] - X[i] for i in range(M-1)]
xd.sort()

if M > N:
    mvcnt = M - N
    print(sum(xd[:mvcnt]))
else:
    print(0)
