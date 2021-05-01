# https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c0f01

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most problems.
t = int(input()) # read a line with a single integer
for x in range(1, t + 1):
    y = int(input())

    def check(x):
        res = False
        n = len(str(x))
        for i in range(1, n//2+1):
            now = int(str(x)[:i]) + 1
            pos = i
            while pos<n:
                nn = len(str(now))
                if pos+nn>n:
                    break
                if int(str(x)[pos:pos+nn])!=now:
                    break
                now += 1
                pos += nn
                if pos==n:
                    res = True
        # print(res, x)
        return res

    ans = y+1
    while(True):
        if check(ans):
            break
        ans += 1
    print("Case #{}: {}".format(x, ans))
    # check out .format's specification for more formatting options
