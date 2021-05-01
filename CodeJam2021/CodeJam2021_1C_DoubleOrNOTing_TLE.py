# https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c0f01
# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most problems.

from queue import Queue

t = int(input()) # read a line with a single integer
for x in range(1, t + 1):
    s, e = input().split()

    def count_change(s):
        ret = 1
        for i in range(len(s)-1):
            if s[i]!=s[i+1]: ret += 1
        return ret

    if s==e:
        ans = 0
    elif count_change(s)<count_change(e):
        ans = 'IMPOSSIBLE'
    else:
        s = int(s, 2)
        e = int(e, 2)
        # print(s, e)
        q = Queue()
        q.put((1, s<<1, False))
        q.put((1, ((1<<(len(bin(s))-2))-1)^s, True))
        while not q.empty():
            cnt, now, flg = q.get()
            # print(cnt, now, e, flg)
            if now==e:
                ans = cnt
                break
            q.put((cnt+1, now<<1, False))
            if not flg:
                q.put((cnt+1, ((1<<(len(bin(now))-2))-1)^now, True))

    print("Case #{}: {}".format(x, ans))
    # check out .format's specification for more formatting options
