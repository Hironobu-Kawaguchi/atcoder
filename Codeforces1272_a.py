# https://codeforces.com/contest/1272/problem/A

def main():
    a, b, c = map(int, input().split())
    ans = 3*10**9
    for i in [1, 0, -1]:
        for j in [1, 0, -1]:
            for k in [1, 0, -1]:
                ans = min(ans, abs(a+i-b-j)+abs(a+i-c-k)+abs(b+j-c-k))
    print(ans)

q = int(input())
for i in range(q):
    main()
