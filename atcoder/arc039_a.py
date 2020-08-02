# https://atcoder.jp/contests/arc039/tasks/arc039_a

A, B = map(int, input().split())
ans = A - B

ans = max(ans, (900+(A%100)) - B)
ans = max(ans, ((A//100)*100+90+(A%10)) - B)
ans = max(ans, ((A//10)*10+9) - B)

ans = max(ans, A - (100+(B%100)))
ans = max(ans, A - ((B//100)*100+(B%10)))
ans = max(ans, A - ((B//10)*10))
print(ans)
