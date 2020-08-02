# https://atcoder.jp/contests/code-festival-2017-quala/tasks/code_festival_2017_quala_b

N, M, K = map(int, input().split())
ans = "No"
for i in range(N+1):
    for j in range(M+1):
        if i*(M-j) + j*(N-i) == K:
            ans = "Yes"
            break
print(ans)
