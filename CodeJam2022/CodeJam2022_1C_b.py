# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877b42/0000000000afe6a1


def solve(x):
    N, K = map(int, input().split())
    E = list(map(int, input().split()))
    sm = 0
    diff = 0
    for i in range(N):
        sm += E[i]
        diff += E[i]*E[i]
    diff -= sm * sm
    if sm==0:
        if diff==0:
            y = 0
        else:
            y = 'IMPOSSIBLE'
    elif diff % (2*sm):
        y = 'IMPOSSIBLE'
    else:
        y = diff // (2*sm)
    print(f"Case #{x}: {y}")

T = int(input())
for t in range(T):
    solve(t+1)
