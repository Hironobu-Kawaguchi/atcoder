# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877ba5/0000000000aa8fc1

t = int(input())
for ti in range(1, t + 1):
    n = int(input())
    b1 = set(range(1, n+1))
    print(*b1, flush=True)
    b2 = list(map(int, input().split()))
    print(*b2, flush=True)
    # print("Case #{}: {}".format(ti, ans))
