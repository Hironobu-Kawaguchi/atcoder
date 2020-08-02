# https://atcoder.jp/contests/abc045/tasks/abc045_b

Sa = input()
Sb = input()
Sc = input()
a, b, c = 0, 0, 0
p = 'a'
ans = ''
while ans == '':
    if p == 'a':
        if a >= len(Sa):
            ans = 'A'
        else:
            p = Sa[a]
            a += 1
    elif p == 'b':
        if b >= len(Sb):
            ans = 'B'
        else:
            p = Sb[b]
            b += 1
    elif p == 'c':
        if c >= len(Sc):
            ans = 'C'
        else:
            p = Sc[c]
            c += 1
    # print(p, a, b, c, ans)

print(ans)
