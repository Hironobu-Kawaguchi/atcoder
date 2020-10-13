# https://atcoder.jp/contests/hhkb2020/tasks/hhkb2020_d

MOD = 10**9+7

def main():
    N, A, B = map(int, input().split())
    r = N-A-B+1
    if r<=0:
        print(0)
        return
    s = r*(r+1)//2
    x = s*(N-B+1)*(N-A+1)
    y = s*s
    ans = 4*x - 4*y
    ans %= MOD
    print(ans)
    return

T = int(input())
for t in range(T):
    main()
