# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4621b

t = int(input())
for x in range(1, t + 1):
    n = int(input())
    s = list(map(int, (input().split())))
    ans = 0
    s.sort()
    for i in range(n):
        if s[i]>=ans+1:
            ans += 1
    print("Case #{}: {}".format(x, ans))
