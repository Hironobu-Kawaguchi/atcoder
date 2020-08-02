# https://atcoder.jp/contests/abc063/tasks/arc075_a

N = int(input())
s = [int(input()) for _ in range(N)]
s.sort()
ans = sum(s)
if ans % 10:
    print(ans)
else:
    for i in range(N):
        if s[i] % 10:
            ans -= s[i]
            print(ans)
            break
    else:
        print(0)
