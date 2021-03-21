# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9f

def main(x):
    S = input()
    y = ''
    now = 0
    for s in S:
        i = int(s)
        if i > now:
            y += '('*(i-now)
        elif i < now:
            y += ')'*(now-i)
        y += s
        now = i
    if now > 0:
        y += ')'*now
    print("Case #{}: {}".format(x, y))

T = int(input())
for i in range(T):
    main(i+1)
