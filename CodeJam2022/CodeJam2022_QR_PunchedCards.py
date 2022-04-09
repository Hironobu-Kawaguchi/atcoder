# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4621b

t = int(input())
for x in range(1, t + 1):
    r, c = [int(s) for s in input().split(" ")]
    ans = [''] * (r*2+1)
    for i in range(r):
        if i==0:
            ans[i*2] += '..+'
            for j in range(c-1):
                ans[i*2] += '-+'
            ans[i*2+1] += '..|'
            for j in range(c-1):
                ans[i*2+1] += '.|'
        else:
            ans[i*2] += '+'
            for j in range(c):
                ans[i*2] += '-+'
            ans[i*2+1] += '|'
            for j in range(c):
                ans[i*2+1] += '.|'
    ans[r*2] += '+'
    for j in range(c):
        ans[r*2] += '-+'
    print("Case #{}:".format(x))
    for a in ans:
        print(a)
