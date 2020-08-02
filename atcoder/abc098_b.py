# https://atcoder.jp/contests/abc098/tasks/abc098_b

N = int(input())
S = input()

ans = 0
for i in range(1, N):
    sj = set()
    sk = set()
    for j in range(i):
        sj.add(S[j])
    for k in range(i, N):
        sk.add(S[k])
    ans = max(len(sj & sk), ans)
    
print(ans)
