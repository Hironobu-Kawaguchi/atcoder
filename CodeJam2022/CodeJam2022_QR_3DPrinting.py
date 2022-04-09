# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4621b

t = int(input())
for x in range(1, t + 1):
    ans = [10**6] * 4
    cmyk = [[int(i) for i in input().split()] for _ in range(3)]
    for i in range(3):
        for j in range(4):
            ans[j] = min(ans[j], cmyk[i][j])
    if sum(ans)<10**6:
        print("Case #{}: IMPOSSIBLE".format(x))
    else:
        rest = sum(ans) - 10**6
        for i in range(4):
            tmp = min(ans[i], rest)
            ans[i] -= tmp
            rest -= tmp
            if rest==0: break
        print("Case #{}: {} {} {} {}".format(x, ans[0], ans[1], ans[2], ans[3]))
