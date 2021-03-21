# https://atcoder.jp/contests/arc083/tasks/arc083_a

A, B, C, D, E, F = map(int, input().split())

x, y, maxe = 0, 0, 0.0

for a in range(F//(A*100)+1):
    for b in range((F-100*A*a)//(B*100)+1):
        for c in range((F-100*(A*a+B*b))//C+1):
            for d in range((F-100*(A*a+B*b)-C*c)//D+1):
                if A*a+B*b == 0:
                    continue
                e = (C*c+D*d) / (A*a+B*b)
                if e <= E and maxe <= e:
                    maxe = e
                    y = C*c+D*d
                    x = 100*(A*a+B*b) + y

print(x, y)
