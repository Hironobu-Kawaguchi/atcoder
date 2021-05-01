# https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c0f00

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most problems.
t = int(input()) # read a line with a single integer
for x in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
    p = list(map(int, input().split()))
    p.sort()
    ys, yss = [], []
    ys.append(p[0]-1)
    ys.append(k-p[-1])
    for i in range(n-1):
        ys.append((p[i+1]-p[i])//2)
        yss.append(p[i+1]-p[i]-1)
    ys.sort(reverse=True)
    yss.sort(reverse=True)
    if n==1:
        ans = (ys[0]+ys[1])/k
    else:
        ans = max(ys[0]+ys[1], yss[0])/k
    print("Case #{}: {}".format(x, ans))
    # check out .format's specification for more formatting options
